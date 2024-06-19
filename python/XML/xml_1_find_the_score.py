import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    result = len(node.attrib.keys())
    for child in node:
        if child:
            result += get_attr_number(child)
        else:
            result += len(child.attrib.keys())

    return result

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))