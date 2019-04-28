import json

data = '''
{
    "name" : "Henri",
    "phone" : {
        "type" : "intl",
        "number" : "+000 000 000 0000"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
print('Phone', info["phone"]["number"],info["phone"]["type"])
