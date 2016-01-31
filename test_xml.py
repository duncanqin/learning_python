#!/usr/bin/python
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
    
tree = ET.ElementTree(file='doc.xml')
root = tree.getroot()
for child_of_root in root:
    print child_of_root.tag,child_of_root.attrib,child_of_root.text