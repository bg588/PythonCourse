# import the built in xml parser from puthon
import xml.etree.ElementTree as ET

data = '''<person>
    <name>Dave</name>
    <phone type="intl">
    +44 7734 303 445
    </phone>
    <email hide="yes">
    dave@smith.com
    </email>
</person>'''

# create a tree from the string
tree = ET.fromstring(data)

# to pull out simple text from that tag
print('Name:', tree.find('name').text)

# to pull out attributes, in this case whether to hide the email
print('Email Hide Attribute:', tree.find('email').get('hide'))

# triple quotes are multi line strings in python. Can be """ or '''
input = '''<stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Dave</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>John</name>
            </user>
        </users>
    </stuff>'''

# create the tree using lib
stuff = ET.fromstring(input)

# create a list of all user tags under users
lst = stuff.findall('users/user')
print('User count:', len(lst))
# each item is a user
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    # can pull out attribute on the user item using get
    print('Attribute is', item.get('x'))
