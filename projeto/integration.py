import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('aqemcasa.xml')
root = tree.getroot()

# Print selected elements and their child elements
def print_selected_elements(element):
    if element.tag == 'address':
        print(f"\n Address: {element.attrib['addr']}")
    elif element.tag == 'osmatch':
        print(f"OS Match Name: {element.attrib['name']}, Accuracy: {element.attrib['accuracy']}")
    elif element.tag == 'port':
        print(f"Port ID: {element.attrib['portid']}, Protocol: {element.attrib['protocol']}")
        service = element.find('service')
        if service is not None:
            print(f"  Service Name: {service.attrib['name']}")

# Traverse the XML tree and print selected elements
def traverse_and_print(element):
    print_selected_elements(element)
    for subelement in element:
        traverse_and_print(subelement)

traverse_and_print(root)
