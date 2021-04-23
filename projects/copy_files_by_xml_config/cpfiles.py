import xml.etree.ElementTree as ET
from pathlib import Path


def copy_file_by_xml_config(source_xml: str, source_tag_name: str, file_name_attribute: str, source_path_attribute: str,
                            destination_path_attribute: str, verbose: bool = False) -> bool:
    """Copies files using data from xml config file
    
       xml format example:
       
       <config>
           <file
               source_path="/var/log"
               destination_path="/etc"
               file_name="server.log"
           />
           ...
       </config>
       
       :param source_xml: xml config file name
       :param source_tag_name: the name of the tag that defines the file
       :param file_name_attribute: the name of the tag attribute that defines the file name to copy
       :param source_path_attribute: the name of the tag attribute that defines the path to source folder
       :param destination_path_attribute: the name of the tag attribute that defines the path to destination folder
       :param verbose: output process information to the console
       :return: False if config file is not found or config file name is empty string else True
    """

    if source_xml == "" or not Path(source_xml).exists():
        return False

    files_number = 0
    files_copied = 0

    for event, elem in ET.iterparse(source_xml):
        if elem.tag == source_tag_name:
            files_number += 1
            try:
                copy_file(*_get_paths_to_files_from_xml(elem, file_name_attribute,
                                                        source_path_attribute, destination_path_attribute))
                files_copied += 1
            except TypeError:
                if verbose:
                    print(f'file {files_number}: Incorrect xml attributes')
                continue
            except FileNotFoundError:
                if verbose:
                    print(f'file {files_number}: Incorrect file data')
            finally:
                elem.clear()
        elem.clear()
        
    if verbose:
        print(f'Files found: {files_number}')
        print(f'Files copied: {files_copied}')

    return True


def _get_paths_to_files_from_xml(xml_elem: ET.Element, file_name_attribute: str, source_path_attribute: str,
                                 destination_path_attribute: str) -> tuple:
    source_folder = Path(xml_elem.get(source_path_attribute))
    destination_folder = Path(xml_elem.get(destination_path_attribute))
    file_name = Path(xml_elem.get(file_name_attribute))

    source_path = Path.joinpath(source_folder, file_name)
    destination_path = Path.joinpath(destination_folder, file_name)

    return source_path, destination_path


def copy_file(source_file_name: str, destination_file_name: str):
    """
    :param source_file_name:  full path to source file
    :param destination_file_name:  full path to destination file
    """
    with open(source_file_name, 'r', encoding='utf-8') as source:
        with open(destination_file_name, 'w', encoding='utf-8') as result:
            for line in source:
                result.write(line)


if __name__ == '__main__':
    pass

