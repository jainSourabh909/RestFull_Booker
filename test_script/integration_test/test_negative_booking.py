from src_framework.constants.apiConstants import url_create_booking
from src_framework.helpers.api_wrapper import post_request
from src_framework.helpers.common_verification import verify_http_method, verify_key_for_not_null_greater_then_zero
from src_framework.helpers.payload_manager import payload_create_booking_negative
from src_framework.helpers.utils import common_headers
import requests
import pytest

class TestCaseNegative(object):
    def test_create_booking_tc1(self):
        response = post_request(url_create_booking(),headers=common_headers(),auth=None,payload=payload_create_booking_negative(),in_json=False)
        print("1-->",response.status_code)
        print("2-->", response.json())
        booking_Id = response.json()['bookingid']
        print("bookingId-->", booking_Id)
        verify_http_method(response,200)
        verify_key_for_not_null_greater_then_zero(booking_Id)
        return booking_Id




