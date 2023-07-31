# help you to read json files and provide you json data
import json


def get_payload_auth():
    ### Read from the auth.json and return,json
    file_data = open(r"src_framework\constants\auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data

def common_headers():
    headers = {
        'Content-Type': 'application/json'
    }
    return headers

def common_headers_for_update_delete_patch(test_post_create_token):
    temp_token = "token=" + test_post_create_token
    print(temp_token)
    headers = {
        'Content-Type': 'application/json',
        "Cookie": temp_token
    }
    return headers