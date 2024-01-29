import xml.etree.ElementTree as ET
import pandas as pd

# Salesforce metadata prefix:
tag_prefix = '{http://soap.sforce.com/2006/04/metadata}'
# Parse the XML file
tree = ET.parse('/Users/angelaldana/Projects/hiberus-sigau/force-app/main/default/permissionsets/ServiceAgentFullAccess.permissionset-meta.xml')
root = tree.getroot()

# Extract the field permissions
data = []
for fieldPermission in root.findall(f'{tag_prefix}fieldPermissions'):
    editable = fieldPermission.find(f'{tag_prefix}editable').text
    field = fieldPermission.find(f'{tag_prefix}field').text
    readable = fieldPermission.find(f'{tag_prefix}readable').text
    data.append([editable, field, readable])

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data, columns=['Editable', 'Field', 'Readable'])

# Write the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)

