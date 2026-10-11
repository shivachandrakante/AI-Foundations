import requests
import json
url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url)
    print(response.status_code)
    print(response.json())
    with open("./session-3/example2.json","w") as file:
        json.dump(response.json(), file, indent = 4)
except Exception as e:
    print(f" Exception message {e}")


