# automation
A repo for automating tasks


## Get Email Alerts for Available GPUs

- Enter your email and username
- If you want, add additional GPU listings or create your own list by inserting links from NewEgg or Bestbuy. Ensure to put each link on its own line.

## Translate a complex XML File

See xml_translate.py:https://github.com/scott-w-maxwell/automation/blob/main/xml_translate.py

- Ensure to install the correct version of googletrans for this: 4.0.0-rc.1
- It should take care of a decent amount of edge cases, but it's not perfect
- Run the script ```python3 xml_tranlsate``` and you will be prompted to enter the language and xml file path
- The completed file will then output to the same directory

## Translate a complex XML file with a text file containing the translations

This allows you to transfer translations within a text file to an XML file. 
To accomplish this, the text from the XML file is translated and then compared to text within the txt file.
If there is a close match, the text in the .txt file is used. Probably not all of it will be translated depending on which accuracy you choose.
Accuracy .60 or higher is recommended. 

Each translation in the .txt file needs to be on it's own line.

- Ensure to install the correct version of googletrans for this: 4.0.0-rc.1
- Run the script ```python3 xml_tranlsate``` and you will be prompted to enter the language, xml file path, accuracy, and text file path
- The completed file will then output to the same directory
