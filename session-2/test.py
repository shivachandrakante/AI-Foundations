import os
import json

with open("session-2/agent-config.json","r") as file:
    data = file.read()
    print(data)
    print(type(data))
    json_type = json.loads(data)
    print(json_type)
    print(type(json_type))