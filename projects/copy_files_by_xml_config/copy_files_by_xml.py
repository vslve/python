import sys

import cpfiles as cp

"""Program copies file using info from xml config file
   If config file name is differ from 'config.xml' pass it as command line argument

   xml format example:
       <config>
           <file
               source_path="/var/log"
               destination_path="/etc"
               file_name="server.log"
           />
           ...
       </config>
    
    if tag name that defines the file or its attributes names are differ from example above
    change it in copy_file_by_xml_config function arguments
"""

source_xml = sys.argv[1] if len(sys.argv) > 1 else 'config.xml'

while True:
    if cp.copy_file_by_xml_config(source_xml, 'file', 'file_name', 'source_path', 'destination_path', True):
        break
    print('Incorrect config file name\nEnter config file name (example: config.xml) or 0 to exit: ')
    source_xml = input()
    if source_xml == '0':
        exit()
