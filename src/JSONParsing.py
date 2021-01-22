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

info = json.loads(date)
# pull out info
print('Name:', info["name"])
# pull out a child
print('Hide Email?', info["email"]["hide"])
