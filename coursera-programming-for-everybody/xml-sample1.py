import xml.etree.ElementTree as ET

data = '''
<person>
    <first_name>Henri</first_name>
    <last_name>Kotka</last_name>
    <phone type="intl">
        +358 000 000 1234
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('first_name').text, tree.find('last_name').text) 
print('Attr (email):', tree.find('email').get('hide'))
print('Phone number:', tree.find('phone').text.strip(), tree.find('phone').get('type'))