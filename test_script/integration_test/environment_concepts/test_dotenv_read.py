import requests
from dotenv import load_dotenv
import pytest
import os

'''
dotenv-->Python-dotenv reads key-value pairs from a .env file and can set them as environment variables.
TO use dotenv we have install it via command--> pip install python-dotenv 
If we have to save all our installed libraries in a file thne we use this command==>pip freeze > requirements.txt
If the token expires in a month or in 10 days or constant then we install it in .env file and if the token changes 
everyday then we have a create a function like 'create_a_token()'.
if we have import lot_dotenv class like this-->from dotenv import load_dotenv
after that we have ton load it after that use it like below--
after load it==>load_dotenv()
get it voa os lib ==> os.getenv("token")
**IMPORTANT-->Change the token if 403 Error is comming.
'''

@pytest.fixture
def test_post_create_booking():
    payload = {
    "firstname" : "Sourabh",
    "lastname" : "Jain",
    "totalprice" : 1234,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2023-07-21",
        "checkout" : "2024-07-29"
    },
    "additionalneeds" : "Breakfast"
    }
    headers = {
        'Content-Type': 'application/json'
    }
    ## header--> Additional info that we need to send to the server to let Server know that we are sending a json payload in the req

    response = requests.post("https://restful-booker.herokuapp.com/booking",json=payload,headers=headers)
    print(response.json())
    booking_Id = response.json()['bookingid']
    print("bookingId-->",booking_Id)
    print("headers-->",response.headers)
    assert response.status_code==200
    return booking_Id

def test_put_update_booking(test_post_create_booking):
    payload = {
        "firstname": "Shahid",
        "lastname": "Kapoor",
        "totalprice": 9999,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-07-21",
            "checkout": "2024-09-29"
        },
        "additionalneeds": "Breakfast Lunch"
    }
    load_dotenv()
    temp_token="token="+os.getenv("token")
    print("temp_token-->",temp_token)
    print("test_post_create_booking-->", test_post_create_booking)

    headers = {
        'Content-Type': 'application/json',
        "Cookie"  : temp_token
    }
    url_put = "https://restful-booker.herokuapp.com/booking/"+str(test_post_create_booking)
    print("url_put-->",url_put)
    response = requests.put(url=url_put, json=payload, headers=headers)
    print("1-->",response.text)
    print("2-->", response.status_code)
    assert response.status_code == 200