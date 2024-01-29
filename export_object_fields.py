import pandas as pd
from simple_salesforce import Salesforce
from utils import getSfAccessToken

# Setup global variables
SF_INSTANCE = 'https://sistemaintegrado--develop.sandbox.my.salesforce.com'
CLI_SF_ORG_DISPLAY = ['sf', 'org', 'display']
CLI_SF_GENERATE_MANIFEST = ['sf', 'project', 'generate', 'manifest', '--type', 'package', '--output-dir', './temp', '--metadata' ]
PACKAGE_XML_PATH = './temp'

def exportObjectFields(object_apiname):
    # Salesforce login details
    sf_session_id = getSfAccessToken()
    sf = Salesforce(instance_url = SF_INSTANCE, session_id = sf_session_id)
    description = None

    # Get object description
    if object_apiname.upper() == 'ACCOUNT':
        description = sf.Account.describe()
    if object_apiname.upper() == 'CONTACT':
        description = sf.Contact.describe()
    if object_apiname.upper() == 'LEAD':
        description = sf.Lead.describe()
    if object_apiname.upper() == 'ACCOUNTCONTACTRELATION':
        description = sf.AccountContactRelation.describe()

    # Extract fields
    fields = description['fields']

    # Prepare data for DataFrame
    data = []

    for field in fields:
        data.append({
            'API Name': field['name'],
            'Label': field['label'],
            'Type': field['type'],
            'Required': not field['nillable'],
            'Unique': field['unique'],
        })

    # Create DataFrame
    df = pd.DataFrame(data)

    # Export to Excel
    df.to_excel(f'object_fields_{object_apiname}.xlsx', index=False)

if __name__ == '__main__':
    object_apiname = input('Objeto a extraer: ')
    exportObjectFields(object_apiname)