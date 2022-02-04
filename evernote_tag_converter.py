import string
import xml.etree.ElementTree as ET
import argparse

parser = argparse.ArgumentParser(description='Convert an Evernote ENEX file with tags that include spaces and/or colons to be Teedy compliant by replacing the spaces with underscores and the colons with a dash - ')
parser.add_argument('url', help="enex file URL", type=str)

args = parser.parse_args()

tree = ET.parse(args.url)
root = tree.getroot()

elems = root.findall(".//tag") #find each tag

for elem in elems: #iterate through the tags and replace the offending charactes
    elem.text = elem.text.replace(' ', '_')
    elem.text = elem.text.replace(':', '-')

tree.write('output.enex') #write the corrected .enex

