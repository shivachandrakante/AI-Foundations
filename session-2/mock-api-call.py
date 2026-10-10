import time

def mock_api_call(payload: dict, simulate_timeout=False, simulate_missing_key=False):

    try:
        if simulate_timeout:
            time.sleep(2)
            raise TimeoutError("LLm API call took too long to respond")
        if simulate_missing_key:
            sample_dict = {"key_1" : "value_1", "key_2": "value_2"}
            key_3 = sample_dict['key_3']
            
    except TimeoutError as e:
        print(f" Timout Errror {e}")
    except KeyError as e:
        print(f" Missing Key Error {e}")

if __name__ == "__main__":
    # Test 1: Simulate a bad JSON output from the LLM
    mock_api_call(payload={"data": "test"}, simulate_missing_key=True)
    
    # Test 2: Simulate a server timeout
    mock_api_call(payload={"data": "test"}, simulate_timeout=True)

    