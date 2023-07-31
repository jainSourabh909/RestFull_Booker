import pytest
import allure
from src_framework.constants.apiConstants import url_create_booking
from src_framework.helpers.api_wrapper import post_request
from src_framework.helpers.common_verification import verify_http_method, verify_key_for_not_null_greater_then_zero
from src_framework.helpers.payload_manager import payload_create_booking
from src_framework.helpers.utils import common_headers

# Declare the global variable booking_id
booking_Id = None
temp_token=None

'''
This file we are use to test allure report.
Step 1==>Install Allure Report:Command(terminal)--> pip install allure-pytest
Step 2==>Install Allure Commandline using npm==>npm i allure-commandline
Step 3==> Import Allure: Statement--> import allure
Step 4==> Mark our Testcase like this:Below Statement
            --> @pytest.mark.smoke
            --> @allure.feature('TC#1--> Verify Create Booking Feature')
            
Step 5==> Run the testcase using below command.(From RestFull Booker Directory)
-->pytest .\test_script\integration_test\test_allure_report.py -v -s --alluredir=./report --html=report.html

Step 6==> Check Wheather node or allue is installed in your system using commnad.
        -->Node = node --version       output = v20.5.0
        -->npm = npm --version         output = 9.8.1
        -->Allure(type allure in your cmd) = allure
Step 7==>Run this command to generate allure report-->allure serve ./report  
Step 8 ==> Stop the Server --> Ctrl + C
    
'''
class TestIntegration(object):

    @pytest.mark.smoke
    @allure.feature('TC#1--> Verify Create Booking Feature')
    def test_create_booking_tc1(self):
        global booking_Id
        response = post_request(url_create_booking(),headers=common_headers(),auth=None,payload=payload_create_booking(),in_json=False)
        print("1-->",response.status_code)
        # print("2-->", response.json())
        booking_Id = response.json()['bookingid']
        print("bookingId-->", booking_Id)
        verify_http_method(response,200)
        verify_key_for_not_null_greater_then_zero(booking_Id)
        # return booking_Id

    @pytest.mark.smoke
    @allure.feature('TC#2--> Verify Create token Feature')
    def test_create_a_token_tc2(self):
        assert True

    @pytest.mark.smoke
    @allure.feature('TC#3--> Verify Put Feature')
    def test_put_tc3(self):
        assert 1==1



    # def test_create_a_token_tc2(self):
    #     global temp_token
    #     response = post_request(url_create_token(),headers=common_headers(),auth=None,payload=payload_create_a_token(),in_json=False)
    #     print("1-->", response.status_code)
    #     verify_http_method(response, 200)
    #     temp_token=response.json()["token"]
    #     print("Token-->",temp_token )
    #     verfiy_token_len_greater_then_zero(temp_token)
    #     # return temp_token
    #
    # def test_put_update_booking_tc3(self):
    #     global temp_token
    #     global booking_Id
    #     print("booking_Id-->",booking_Id)
    #     response = put_request(url_update_delete_booking(booking_Id),headers=common_headers_for_update_delete_patch(temp_token),auth=None,payload=payload_put_update_a_booking(),in_json=False)
    #     print("1-->",response.status_code)
    #     print("2-->", response.json())
    #     verify_http_method(response,200)
    #
    # def test_patch_update_booking_tc4(self):
    #     global temp_token
    #     global booking_Id
    #     print("booking_Id-->", booking_Id)
    #     response = patch_request(url_update_delete_booking(booking_Id),headers=common_headers_for_update_delete_patch(temp_token),auth=None,payload=payload_patch_update_a_booking(),in_json=False)
    #     print("1-->",response.status_code)
    #     print("2-->", response.json())
    #     verify_http_method(response,200)
    #
    # def test_delete_booking_tc5(self):
    #     global temp_token
    #     global booking_Id
    #     print("booking_Id-->", booking_Id)
    #     response = delete_request(url_update_delete_booking(booking_Id),headers=common_headers_for_update_delete_patch(temp_token),auth=None,in_json=False)
    #     print("1-->",response.status_code)
    #     print("2-->", response.text)
    #     verify_http_method(response,201)
    #
    # def test_get_deleted_booking_id_tc6(self):
    #     global booking_Id
    #     print("booking_Id-->", booking_Id)
    #     response = get_request(url_update_delete_booking(booking_Id),auth=None,in_json=False)
    #     print("1-->",response.status_code)
    #     print("2-->",response.text)
    #     verify_http_method(response,404)








