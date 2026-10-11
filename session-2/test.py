import os
import json
from dataclasses import dataclass, asdict

try:
    with open("ssession-2/agent-config.json","r") as file:
        data = file.read()
        print(data)
        print(type(data))
        json_type = json.loads(data)
        print(json_type)
        print(type(json_type))
except Exception as e:
    print(f"Error messge {e}")

