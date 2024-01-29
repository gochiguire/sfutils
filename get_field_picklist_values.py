import xml.etree.ElementTree as ET
import pandas as pd

# Salesforce metadata prefix:
tag_prefix = '{http://soap.sforce.com/2006/04/metadata}'

# Parse the XML file
tree = ET.parse('/Users/angelaldana/Projects/hiberus-sigau/force-app/main/default/objects/AccountContactRelation/fields/Tipo__c.field-meta.xml')
root = tree.getroot()

# Extract the picklist values
picklist_values = []
for value in root.findall(f'.//{tag_prefix}valueSetDefinition/{tag_prefix}value'):
    full_name = value.find(f'{tag_prefix}fullName').text
    default = value.find(f'{tag_prefix}default').text
    label = value.find(f'{tag_prefix}label').text
    picklist_values.append([full_name, default, label])

# Print the picklist values
for value in picklist_values:
    print(f"{value[0]}")

