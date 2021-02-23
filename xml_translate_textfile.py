import xml.etree.ElementTree as ET 
from bs4 import BeautifulSoup as soup
from difflib import SequenceMatcher
from googletrans import Translator
import html
import bs4
import re

xml_file = input("Enter XML file name/path: ")
text_file = input("Enter Text file name/path: ")
accuracy = float(input("Enter accuracy: "))

# Open the XML file as an ElementTree
tree=ET.parse(xml_file)
root = tree.getroot()

# Convert ElementTree string (unicode)
xmlstr = ET.tostring(root, encoding='unicode', method='xml')
xmlstr = html.unescape(xmlstr)

# Open Text File as list
trans_list = []
with open(text_file, 'r', encoding='utf-8') as temp:
	for line in temp:
		if line != '\n':
			trans_list.append(line.replace('\n',''))

not_translated = []
translated = {}
def translate(text):
    global translated
    global lang
    global accuracy

    # Check to see if translation has already been done
    if text in translated:
        return translated[text]

    # Use GTranslate and compare with list of translations
    translator = Translator(service_urls=['translate.google.com'])
    translated_text = translator.translate(text, dest=f'{lang}').text
    for line in trans_list:
    	
        # Found directly in the list
        if translated_text == line:
            translated[text] = line
            return line
            
        if SequenceMatcher(None, translated_text, line).ratio() > accuracy:

            translated[text] = line
            return line
    return

def parse_root(x):

    global xmlstr
    global not_translated

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
                    else:
                        not_translated.append(elem_text)
                        
        # Call function recursively
        parse_root(child)

# parse ElementTree root
parse_root(root)

print("\nNOT TRANSLATED:", len(revised_not_translated))

# DO NOT RUN THIS CODE
Save XML string as XML file
with open(f"{file_name}_{lang}.xml", "wb") as f:
	f.write(xmlstr.encode('utf-8'))