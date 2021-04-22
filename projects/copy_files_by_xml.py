import sys

import xml.etree.ElementTree as ET
from pathlib import Path

"""Program copies files using data from xml config file
    xml format example:

    <config> 
        <file 
            source_path="/var/log" 
            destination_path="/etc" 
            file_name="server.log" 
        /> 
        ...
    </config>

"""

source_xml = sys.argv[1] if len(sys.argv) > 1 else 'config.xml'
source_tag_name = 'file'

attributes_names = {
    'source': 'source_path',
    'destination': 'destination_path',
    'file': 'file_name'
}

file_number = 1

for event, elem in ET.iterparse(source_xml):
    if elem.tag == source_tag_name:
        source = Path(elem.get(attributes_names['source']))
        destination = Path(elem.get(attributes_names['destination']))
        file = Path(elem.get(attributes_names['file']))

        source_path = Path.joinpath(source, file)
        destination_path = Path.joinpath(destination, file)

        try:
            with open(source_path, 'r', encoding='utf-8') as source:
                with open(destination_path, 'w', encoding='utf-8') as result:
                    for line in source:
                        result.write(line)
        except FileNotFoundError:
            print(f'file {file_number}: Incorrect file data')
        finally:
            file_number += 1
            elem.clear()