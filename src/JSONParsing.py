import json

date = '''{
        "name" : "James",
        "phone" : {
            "type" : "intl",
            "number" : "+44 7734 303445"
            },
        "email" : {
                "hide" : "yes"
            }
        }'''

# use loads to load from string, info is a dictionary
info = json.loads(date)
# pull out name
print('Name:', info["name"])
# pull out a child - hide from email
print('Hide Email?', info["email"]["hide"])

# this time input is a list of JSON
input = '''[
        { "id" : "001",
          "x" : "2",
          "name" : "Dave"
        } ,
        { "id" : "009",
          "x" : "7",
          "name" : "John"
        }
        ]'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
