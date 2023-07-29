'''
Author  : Sourabh Jain
Objective : Create and Verify by Post Request
TC#1 = Verify the Status Code , headers
TC#2 = Verify the Body --> Booking Id
TC#3 = Verify the JSON Schema is Valid
@pytest.mark.run(order=1) = USED to run test case in order
'''
import requests
import pytest

from src.constants.apiConstants import url_create_booking, url_create_token, url_update_delete_booking
from src.helpers.api_wrapper import post_request, put_request, delete_request, patch_request
from src.helpers.common_verification import verify_http_method, verify_key_for_not_null_greater_then_zero, \
    verfiy_token_len_greater_then_zero
from src.helpers.payload_manager import payload_create_booking, payload_create_a_token, payload_put_update_a_booking, \
    payload_patch_update_a_booking

from src.helpers.utils import common_headers, common_headers_for_update_delete_patch
'''
command to run the test case in terminal inside integration_test directory ==> pytest -n auto -v -s --html=report.html
 

'''

class TestIntegration(object):
    @pytest.fixture
    def test_create_booking_tc1(self):
        response = post_request(url_create_booking(),headers=common_headers(),auth=None,payload=payload_create_booking(),in_json=False)
        print("1-->",response.status_code)
        # print("2-->", response.json())
        booking_Id = response.json()['bookingid']
        print("bookingId-->", booking_Id)
        verify_http_method(response,200)
        verify_key_for_not_null_greater_then_zero(booking_Id)
        return booking_Id

    @pytest.fixture
    def test_create_a_token_tc2(self):
        response = post_request(url_create_token(),headers=common_headers(),auth=None,payload=payload_create_a_token(),in_json=False)
        print("1-->", response.status_code)
        verify_http_method(response, 200)
        temp_token=response.json()["token"]
        print("Token-->",temp_token )
        verfiy_token_len_greater_then_zero(temp_token)
        return temp_token

    def test_put_update_booking_tc3(self,test_create_booking_tc1,test_create_a_token_tc2):
        # test_create_booking_tc1= self.test_create_booking_tc1()
        # test_create_a_token_tc2=self.test_create_a_token_tc2()
        # print("test_create_booking_tc1",test_create_booking_tc1)
        # print("test_create_a_token_tc2",test_create_a_token_tc2)
        response = put_request(url_update_delete_booking(test_create_booking_tc1),headers=common_headers_for_update_delete_patch(test_create_a_token_tc2),auth=None,payload=payload_put_update_a_booking(),in_json=False)
        print("1-->",response.status_code)
        print("2-->", response.json())
        verify_http_method(response,200)

    def test_patch_update_booking_tc4(self,test_create_booking_tc1,test_create_a_token_tc2):
        response = patch_request(url_update_delete_booking(test_create_booking_tc1),headers=common_headers_for_update_delete_patch(test_create_a_token_tc2),auth=None,payload=payload_patch_update_a_booking(),in_json=False)
        print("1-->",response.status_code)
        print("2-->", response.json())
        verify_http_method(response,200)

    def test_delete_booking_tc5(self,test_create_booking_tc1,test_create_a_token_tc2):
        response = delete_request(url_update_delete_booking(test_create_booking_tc1),headers=common_headers_for_update_delete_patch(test_create_a_token_tc2),auth=None,in_json=False)
        print("1-->",response.status_code)
        verify_http_method(response,201)








