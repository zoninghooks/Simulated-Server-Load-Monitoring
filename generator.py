import json
import random
servers = {}

for server in range(10):
    alltheservers = ("server" + str(server))
    servers[alltheservers] = random.randint(0,100)

with open("data.json","w") as file:
    json.dump(servers, file)