from pydantic import BaseModel, ValidationError
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

class userInsight(BaseModel):
    user_name: str
    sentiment_score: int
    is_flagged_for_review: bool

print(" --- Model Initilized --- ")
print(userInsight.model_json_schema())

def analyze_user_data_via_api():
    headers = {
        "content-type" :"application/json",
        "Authorization" : "Bearer sk-mock-api-key-12345"
    }
    payload = {
        "model" : "gpt-4-flash-lite",
        "messages" : [
            {
                "role" : "system",
                "content": "you Analyze user sentiment"
            },
            {
                "role": "user",
                "content": "analyze the sentiment for user 'Alice"
            }
        ]
    }

    print("-- Transmitting the HTTP post request -- ")

    try:
        response = requests.post(API_URL, headers=headers,json=payload, timeout=5)
        response.raise_for_status()
        print(f"Call sucess - Statuss code {response.status_code}")
        mock_ll_output = {
            "user_name" : "Alice",
            "sentiment_score" : "88",
            "is_flagged_for_review" : "false"
        }
        return mock_ll_output
    except requests.exceptions.RequestException as e:
        print(f"[NETWORK CRASH] Failed to reach API: {e}")
        return None

if __name__ == "__main__" :
    raw_api_data = analyze_user_data_via_api()
    if raw_api_data:
        print(" -- Vladiting Raw LLM Output")
        print(f" Raw Data recieved: {raw_api_data} \n ")
    try : 
        Validated_insight = userInsight(**raw_api_data)
        print(" -- Validation Succesful -- ")
        print(f" Second Object : {Validated_insight}")

        print(f" Cleaned Score : {Validated_insight.sentiment_score + 10}")
    except ValidationError as e:
        print(f"[Validation Crash] The LLM failed to match our schema : \n {e.json()}")

