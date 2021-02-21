import xml.etree.ElementTree as ET 
from bs4 import BeautifulSoup as soup
from googletrans import Translator #This needs to be version: 4.0.0-rc.1
import html
import bs4

lang = input("Language: ").lower()
file_name = input("File Path: ")

# Open the XML file as an ElementTree
tree=ET.parse(f'{os}Tree.xml')
root = tree.getroot()

# Convert ElementTree to a string
xmlstr = ET.tostring(root, encoding='unicode', method='xml')
xmlstr = html.unescape(xmlstr)


def translate(text):

    global lang

    # Use GTranslate and compare with list of translations
    translator = Translator(service_urls=['translate.google.com'])
    translated_text = translator.translate(text, dest=f'{lang}').text

    return translated_text

def parse_root(x):

    global xmlstr

    for child in x:

        split_text = child.text.split('\n')

        for elem in split_text:

            if 'http' not in elem:
                elem_text = soup(elem, 'html.parser').text

                # remove spaces on ends
                elem_text = elem_text.rstrip().lstrip()

                # ensure words are in string
                if any(a.isalpha() for a in elem_text):
                    translation = translate(elem_text)
                    if translation:
                        xmlstr = xmlstr.replace(elem_text, translation)
                        
        # Call function recursively
        parse_root(child)


# parse ElementTree root
parse_root(root)

# Save XML string as XML file
with open(f"{lang}_translated_to_{lang}.xml", "wb") as f:
	f.write(xmlstr.encode('utf-8'))