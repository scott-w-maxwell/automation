import xml.etree.ElementTree as ET 
from bs4 import BeautifulSoup as soup
from googletrans import Translator #This needs to be version: 4.0.0-rc.1
import html
import bs4
import re


lang = input("Language to translate to: ").lower()
file_name = input('File Name: ')

def translate(text lang):

    # Use GTranslate and compare with list of translations
    translator = Translator(service_urls=['translate.google.com'])
    translated_text = translator.translate(text, dest=f'{lang}').text

    return translated_text


def parse_root(file_name, lang):

	# Open the XML file as an ElementTree
	tree=ET.parse(f'{file_name}')
	root = tree.getroot()

	# Convert ElementTree to string
	xmlstr = ET.tostring(root, encoding='unicode', method='xml')
	xmlstr = html.unescape(xmlstr)

    for child in tree:

        split_text = child.text.split('\n')

        for elem in split_text:

        	# Ensuring not to translate links. (also avoids bs4 warning)
            if 'http' not in elem:
                elem_text = soup(elem, 'html.parser').text

                # remove spaces on ends
                elem_text = elem_text.rstrip().lstrip()

                # ensure words are in string
                if any(a.isalpha() for a in elem_text):
                    translation = translate(elem_text, lang)
                    if translation:
                        xmlstr = xmlstr.replace(elem_text, translation)
                        
        # Call function on children
        parse_root(child)

	# Save XML string as XML file
	with open(f"/Finished/{file_name}_translated.xml", "wb") as f:
		f.write(xmlstr.encode('utf-8'))

