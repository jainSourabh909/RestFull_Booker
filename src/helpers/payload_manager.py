
def payload_create_booking():
    ### in future we will replace it from json
    payload = {
        "firstname": "Sourabh",
        "lastname": "Jain",
        "totalprice": 1234,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-07-21",
            "checkout": "2024-07-29"
        },
        "additionalneeds": "Breakfast"
    }
    return payload

def payload_create_booking_negative():
    ### in future we will replace it from json
    first_name=eval(input("enter a first_name-->"))
    last_name = eval(input("enter a last_name-->"))
    payload = {
        "firstname": first_name,
        "lastname": last_name,
        "totalprice": 1234,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-07-21",
            "checkout": "2024-07-29"
        },
        "additionalneeds": "Breakfast"
    }
    return payload

def payload_create_a_token():
    payload = {
    "username" : "admin",
    "password" : "password123"
    }
    return payload

def payload_put_update_a_booking():
    ### in future we will replace it from json
    payload = {
        "firstname": "Shahid",
        "lastname": "Kapoor",
        "totalprice": 9999,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-07-24",
            "checkout": "2025-07-27"
        },
        "additionalneeds": "Breakfast Lunch"
    }
    return payload

def payload_patch_update_a_booking():
    ### in future we will replace it from json
    payload = {
        "firstname": "Vicky",
        "lastname": "Kaushal",
        "additionalneeds": "Breakfast Lunch Dinner"
    }
    return payload

