
import pytest
import requests
import json

url = "https://census-toy.nceng.net/prod/toy-census"


# Test how API responds to the empty body
def test_api_response_empty_body():
    response = requests.post(url)
    assert response.status_code == 400  # Expecting a 400 Bad Request due to missing required fields


# Test if the API returns the correct response for CountByGender action type
def test_count_by_gender():
    data = {
        "actionType": "CountByGender",
        "users": [
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "other"}
        ]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    returning_data = response.json()
    assert {"name": "male", "value": 2} in returning_data
    assert {"name": "female", "value": 1} in returning_data
    assert {"name": "other", "value": 1} in returning_data


# Test if the API returns the correct response for CountByCountry action type
def test_count_by_country():
    data = {
        "actionType": "CountByCountry",
        "users": [
            {"nat": "US"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"}
        ]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    returning_data = response.json()
    assert {"name": "US", "value": 2} in returning_data
    assert {"name": "UK", "value": 1} in returning_data
    assert {"name": "CA", "value": 1} in returning_data


# Test if the API returns the correct response for CountPasswordComplexity action type
def test_count_password_complexity():
    data = {
        "actionType": "CountPasswordComplexity",
        "users": [
                {"login": {"password": "abc123"}},
                {"login": {"password": "abc#$!"}},
                {"login": {"password": "ab12*@"}}
        ]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    returning_data = response.json()
    assert {"name": "abc123", "value": 0} in returning_data
    assert {"name": "abc#$!", "value": 3} in returning_data
    assert {"name": "ab12*@", "value": 2} in returning_data


# Test how API responds to the missing required fields of users for CountByGender action type
def test_count_by_gender_missing_req_field():
    data = {
        "actionType": "CountByGender",
        "users": [
            {},
            {},
            {},
            {}  # Missing "gender" - required  field
        ]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400


# Test if the API returns the correct response for CountByGender action type with invalid gender values
def test_count_by_gender_invalid_values():
    data = {
        "actionType": "CountByGender",
        "users": [
            {"gender": "M"},
            {"gender": "F"},
            {"gender": "M"},
            {"gender": "unknown"}
        ]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400
    # returning_data = response.json()
    # assert {"name": "male", "value": 2} in returning_data
    # assert {"name": "female", "value": 1} in returning_data
    # assert {"name": "other", "value": 1} in returning_data


#  Test how API responds to the missing "users" array
def test_count_by_gender_missing_users():
    data = {
        "actionType": "CountByGender"
        # Missing "users" array
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400


# Test what happens when all the records  have a gender value of "male"
def test_count_by_gender_all_male():
    data = {
        "actionType": "CountByGender",
        "users": [
            {"gender": "male"},
            {"gender": "male"},
            {"gender": "male"},
            {"gender": "male"}
        ]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    result = response.json()
    assert len(result) == 1  # Expected only one record
    assert {"name": "male", "value": 4} in result
    assert {"name": "female", "value": 0} not in result
    assert {"name": "other", "value": 0} not in result


# Test what happens when all the records  have a gender value of "female"
def test_count_by_gender_all_female():
    data = {
        "actionType": "CountByGender",
        "users": [
            {"gender": "female"},
            {"gender": "female"},
            {"gender": "female"},
            {"gender": "female"},
            {"gender": "female"},
            {"gender": "female"},
            {"gender": "female"}
        ]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    result = response.json()
    assert len(result) == 1  # Expected only one record
    assert {"name": "female", "value": 7} in result


#  Test how API responds to the invalid country codes
def test_count_by_country_invalid_country_code():
    data = {
        "actionType": "CountByCountry",
        "users": [
            {"nat": "US"},
            {"nat": "UK"},
            {"nat": "USA"},
            {"nat": "AU"},
            {"nat": "AU"},
            {"nat": "CA"}
        ]
    }
    response = requests.post(url, json=data)
    # assert response.status_code == 400
    returning_data = response.json()
    assert {"name": "US", "value": 1} in returning_data
    assert {"name": "UK", "value": 1} in returning_data
    assert {"name": "AU", "value": 2} in returning_data
    assert {"name": "CA", "value": 1} in returning_data
    assert {"name": "USA", "value": 1} not in returning_data


# Test how API responds to the empty country count
def test_count_by_empty_country_count():
    data = {
        "actionType": "CountByCountry",
        "users": [

        ]  # Empty nat(country) data
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400


# Test how API responds to the missing required fields
def test_count_by_country_missing_req_fields():
    data = {
        "actionType": "CountByCountry",
        "users": [
            {},
            {},
            {},
            {},
            {}
        ]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400


# Test response format and data integrity
def test_count_password_complexity_response_format():
    data = {
        "actionType": "CountPasswordComplexity",
        "users": [
            {"login": {"password": "xyz123"}},
            {"login": {"password": "@bc#"}},
            {"login": {"password": "000#$%"}}
        ]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    returning_data = response.json()

    # Verification of response format
    assert isinstance(returning_data, list)  # Expecting a list of records
    assert all(isinstance(record, dict) for record in returning_data)  # Each record should be a dictionary

    # Verification of data integrity
    password_complexity = {
        "xyz123": 0,
        "@bc#": 2,
        "000#$%": 3
    }
    for record in returning_data:
        name = record["name"]
        value = record["value"]
        assert name in password_complexity  # Ensure the password is present in the expected scores
        assert value == password_complexity[name]  # Compare the expected complexity score for the password


# Test if the result is valid per top parameter in CountByCountry actionType
def test_valid_top_parameter_count_by_country():
    data = {
        "actionType": "CountByCountry",
        "users": [
            {"nat": "US"},
            {"nat": "UK"},
            {"nat": "AU"},
            {"nat": "AU"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "US"},
            {"nat": "US"},
            {"nat": "NZ"},
            {"nat": "AE"},
            {"nat": "MC"}
        ],
        "top": 3
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    result = response.json()
    assert len(result) == 3


# Test how API responds to the negative top parameter of CountByCountry action type
def test_negative_top_parameter_count_by_country():
    top = -3
    data = {
        "actionType": "CountByCountry",
        "users": [
            {"nat": "US"},
            {"nat": "UK"},
            {"nat": "EG"},
            {"nat": "US"},
            {"nat": "US"},
            {"nat": "IT"},
            {"nat": "UK"},
            {"nat": "IT"},
            {"nat": "IT"},
            {"nat": "IT"},
            {"nat": "AE"},
            {"nat": "ZM"}
        ],
        "top": top
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400


# Test how API responds to the negative top parameter of CountByGender action type
def test_negative_top_parameter_count_by_gender():
    data = {
        "actionType": "CountByGender",
        "users": [
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "other"}
        ],
        "top": -1
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400


# Test top parameter equals to 0 of CountByGender actionType
def test_zero_top_parameter_count_by_gender():
    data = {
        "actionType": "CountByGender",
        "users": [
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "other"}
        ],
        "top": 0
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400


# Test if the result is valid per top parameter in CountByGender actionType
def test_top_parameter_count_by_gender():
    data = {
        "actionType": "CountByGender",
        "users": [
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "other"}
        ],
        "top": 1
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    returning_data = response.json()
    assert len(returning_data) == 1
    assert returning_data[0]["name"] == "male"
    assert returning_data[0]["value"] == 2


# Test top parameter with invalid value for CountByGender actionType
def test_invalid_top_parameter_count_by_gender():
    data = {
        "actionType": "CountByGender",
        "users": [
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "other"}
        ],
        "top": "male"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400


# Test top parameter with max value for CountByGender actionType
def test_max_top_parameter_count_by_gender():
    data = {
        "actionType": "CountByGender",
        "users": [
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "other"}
        ],
        "top": 4
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400
