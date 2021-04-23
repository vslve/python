"""
Program copies file using info from xml config file
 
To run the program enter program name and its args: 

    program.py config_file.xml file_tag file_name_attr source_path_attr destination_path_attr 

file_tag: the name of the xml tag that defines the file
file_name_attr: the name of the file_tag attribute that defines the file name to copy
source_path_attr: the name of the file_tag attribute that defines the path to source folder
destination_path_attr: the name of the file_tag attribute that defines the path to destination folder 

Example:

    program name: copy.py
    config xml file name: config.xml
    
    config xml file format:
    
       <config>
           <file
               source_path="/var/log"
               destination_path="/etc"
               file_name="server.log"
           />
           ...
       </config>
       
    command to run: copy.py config.xml file file_name source_path destination_path

If name of the file_tag and names of the file_tag attributes do not differ from the example config xml
it can be omitted: 
    
                    copy.py config.xml
"""

default_args = ('file', 'file_name', 'source_path', 'destination_path')


def main():
    args = sys.argv[1:]
    argc = len(args)

    if argc == 0:
        print('Enter config xml file name to copy files or -usage to show program usage guide: ')
        args.append(input())
        argc += 1
    if args[0] == '-usage':
        print(__doc__)
        return
    if argc == 1:
        args.extend(default_args)

    try:
        if not cp.copy_file_by_xml_config(*args, verbose=True):
            print('Incorrect config file name')
    except TypeError:
        print('Incorrect args')
    finally:
        print(f'\nEnter program_name.py -usage to show program usage guide')


if __name__ == '__main__':
    import sys

    import copy_files as cp

    main()
