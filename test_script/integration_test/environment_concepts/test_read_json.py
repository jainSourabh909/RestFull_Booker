import json

import requests
from dotenv import load_dotenv
import pytest
import os


'''
In this file we are taking data from two json files and switching them via .env varibales.
We are giving variables like "load_env" in dotenv give file name.
after that we are using it in test_read_json.py file after loading it.
Means We can take dat from json file Also.
'''

@pytest.fixture
def load_json_data():
    assert 1 == 1
    # load_dotenv()
    # file_name = os.getenv("load_env")
    # with open(file_name, 'r') as f:
    #     data = json.load(f)
    # return data

def test_make_req(load_json_data):
    assert 1==1
    # print("\nload_json_data==>",load_json_data)
    # print("env_url==>",load_json_data["url"])