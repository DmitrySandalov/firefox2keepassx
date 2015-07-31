from xml.dom import minidom
import xml.etree.cElementTree as ET

xml_doc = minidom.parse('data.xml')
item_list = xml_doc.getElementsByTagName('entry')


root = ET.Element("database")

doc = ET.SubElement(root, "group")
web = ET.SubElement(doc, "title").text = "web"
web = ET.SubElement(doc, "icon").text = "0"

for s in item_list:
    print(s.attributes['host'].value)
    entry = ET.SubElement(doc, "entry")

    ET.SubElement(entry, "title").text = s.attributes['host'].value
    ET.SubElement(entry, "username").text = s.attributes['user'].value
    ET.SubElement(entry, "password").text = s.attributes['password'].value
    ET.SubElement(entry, "url").text = s.attributes['formSubmitURL'].value
    ET.SubElement(entry, "comment").text = ""
    ET.SubElement(entry, "icon").text = "0"
    ET.SubElement(entry, "creation").text = "2015-07-30T01:02:01"
    ET.SubElement(entry, "lastaccess").text = "2015-07-30T01:03:10"
    ET.SubElement(entry, "lastmod").text = "2015-07-30T01:03:10"
    ET.SubElement(entry, "expire").text = "2999-12-27T23:59:59"

tree = ET.ElementTree(root)
tree.write("out.xml")

