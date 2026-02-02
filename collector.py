import json
import requests

r = requests.get("http://34.173.238.140/data.json").json()

#{'server0': 25, 'server1': 24, 'server2': 66, 'server3': 57, 'server4': 12, 'server5': 17, 'server6': 12, 'server7': 48, 'server8': 22, 'server9': 3}
utilised = {"over":0 , "under":0}

for server in r: 
    print(server)
    number = r[server]
    if number <= 49:
        utilised["under"] = utilised["under"] + 1 
    else:
        utilised["over"] = utilised["over"] + 1
    
print (utilised)
#if the number is equal or less than 49 then add to "under"
#if the number is equal or greather than 50 then add to "over"

