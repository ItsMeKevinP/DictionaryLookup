import json

import requests

app_id = "ENTER API KEY HERE"
app_key = "ENTER APP KEY HERE"

urlBase = "https://od-api.oxforddictionaries.com:443/api/v1/entries/"

languages = {"english": "en", "spanish": "es", "german": "de"}
lan = input("Choose a language: English || Spanish || German\n").lower()

while lan not in languages.keys():
    lan = input("Choose a language: English || Spanish || German\n").lower()

print("Language Chosen: %s\n" % lan.capitalize())

urlLang = languages.get(lan)

word = input("What word would you like to look up?\n").lower()

print("\033[1m\033[4m", "Results for ➤", word.capitalize(), "\033[0m\n")

lookupUrl = urlBase + urlLang + '/' + word
req = requests.get(lookupUrl, headers={"app_id": app_id, "app_key": app_key})
# JSON to String
try:
    req = json.dumps(req.json())
except ValueError:
    if req.status_code == 404:
        exit("Word Unavailable")
    if req.status_code == 500:
        exit("Internal Server Error")
# JSON to Dict
req = json.loads(req)
count = 0
subCount = 0
# print(type(req))
# navigating this JSON file was crazy
for values in req['results'][0]['lexicalEntries']:
    for values2 in req['results'][0]['lexicalEntries'][count]['entries'][0]['senses']:
        subCount += 1
        print("\033[1mDefinition", subCount, ":\033[0m \n\t", values2['definitions'][0].capitalize())

    count += 1

