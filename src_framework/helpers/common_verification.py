

def verify_http_method(response_data,expected_data):
    assert response_data.status_code == int(expected_data),"Expected HTTP Status : " + expected_data

## Any key should not be null or empty

def verify_key_for_not_null_greater_then_zero(key):
    assert key != 0,"Key is not empty : " + key
    assert key>0,"Key should be greater then zero: " + key

def verfiy_token_len_greater_then_zero(token):
    assert len(token) > 0,"token is not empty : " + token

