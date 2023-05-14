# Census Toy API service 

## For testing the Census Toy API service were used and why:
	Programming language - Python
	Framework - Pytest
	IDE - PyCharm
	Python Interpreter - Anaconda

Pytest is a popular testing framework for Python that makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries. Pytest uses plain assert statements and provides detailed assertion introspection. Pytest also supports many plugins and features that enhance its functionality and usability.


## How is it run?

### You will need:
PyCharm IDE https://www.jetbrains.com/pycharm/download/
Anaconda https://www.anaconda.com/download
### Steps to run:
- Launch PyCharm IDE
- Install Pytest library using (in the terminal)
```bash
pip install pytest
```
- Install Requests library using (in the terminal)
```bash
pip install requests
``` 

- Open project using "File > Open > Choose unzipped folder"
- If "test_census_toy_api_service.py"file is opened
- Run the test scripts in terminal using (in the terminal)
```bash 
pytest -v ./test_census_toy_api_service.py
```


## Summary of test results:
Collected 20 items for what worked with the Census Toy API service and what did not.                                                                                            
```
test_api.py::test_api_response_empty_body FAILED                                                         [  5%]
test_api.py::test_count_by_gender PASSED                                                                 [ 10%]
test_api.py::test_count_by_country PASSED                                                                [ 15%]
test_api.py::test_count_password_complexity FAILED                                                       [ 20%]
test_api.py::test_count_by_gender_missing_req_field FAILED                                               [ 25%]
test_api.py::test_count_by_gender_invalid_values FAILED                                                  [ 30%]
test_api.py::test_count_by_gender_missing_users FAILED                                                   [ 35%]
test_api.py::test_count_by_gender_all_male PASSED                                                        [ 40%]
test_api.py::test_count_by_gender_all_female PASSED                                                      [ 45%]
test_api.py::test_count_by_country_invalid_country_code FAILED                                           [ 50%]
test_api.py::test_count_by_empty_country_count FAILED                                                    [ 55%]
test_api.py::test_count_by_country_missing_req_fields FAILED                                             [ 60%]
test_api.py::test_count_password_complexity_response_format FAILED                                       [ 65%]
test_api.py::test_valid_top_parameter_count_by_country FAILED/PASSED                                     [ 70%]
test_api.py::test_negative_top_parameter_count_by_country FAILED                                         [ 75%]
test_api.py::test_negative_top_parameter_count_by_gender FAILED                                          [ 80%]
test_api.py::test_zero_top_parameter_count_by_gender FAILED                                              [ 85%]
test_api.py::test_top_parameter_count_by_gender PASSED                                                   [ 90%]
test_api.py::test_invalid_top_parameter_count_by_gender FAILED                                           [ 95%]
test_api.py::test_max_top_parameter_count_by_gender FAILED                                               [100%]
```


## Description of bugs(failed test cases):

### **Test case:** test_api_response_empty_body

**Title:** Incorrect API response to the empty body

**Description:**
	When sending an empty body request, the API should return a 400 - Bad Request [A syntax error in the client's request] status code. However, it returns 200 - OK status code.

**Steps to reproduce:**
1. 	Send an empty body POST request to the API.
2. 	Observe the issue.

**Expected result:** Should return 400 status code of Bad request

**Actual result:** Returns 200 OK status code


### **Test case:** test_count_password_complexity

**Title:** API returns the incorrect result for CountPasswordComplexity action type

**Description:**
	When sending request for CountPasswordComplexity actionType an API returns incorrect count of non-alphanumeric characters in the password 

**Steps to reproduce:**
1. 	Send an HTTP POST request with some users' password data to the API.
2. 	Get the result
3. 	Observe the issue.

**Expected result:** Should return the correct number of non-alphanumeric characters in the password

**Actual result:** Returns incorrect number of non-alphanumeric characters in the password


### Test case: test_count_by_gender_missing_req_field

**Title:** API returns 200 OK status code to the missing required field "gender"

**Description:** While testing CountByGender actionType with the missing required field API returns 200 OK status code with the count of null values.

**Steps to reproduce:**
1. 	Send an HTTP POST request with missing required "gender" fields to the API.
2. 	Get the result
3. 	Observe the issue.

**Expected result:** Should return 400 Bad request because of missing required fields

**Actual result:** Returns 200 OK status code with count of null values


### Test case: test_count_by_gender_invalid_values

**Title:** API returns 200 OK status code for CountByGender actionType with invalid values

**Description:** API returns 200 OK status code and counts values while testing CountByGender actionType with invalid values.

**Steps to reproduce:**
1. 	Send an HTTP Post request for ContByGender actionType with invalid gender values
2. 	Observe the issue.

**Expected result:** Should return 400 Bad request for invalid ender values
**Actual result:** Returns 200 OK status code


### Test case: test_count_by_gender_missing_users

**Title:** API returns 200 OK status code for CountByGender actionType with missing users array

**Description:** API returns 200 OK status code while testing CountByGender actionType with missing users' array.

**Steps to reproduce:**
1. 	Send an HTTP Post request for ContByGender actionType without users' data
2. 	Observe the issue.

**Expected result:** Should return 400 Bad request for missing users' array

**Actual result:** Returns 200 OK status code

                                                
### Test case: test_count_by_country_invalid_country_code

**Title:** API returns 200 OK status code and counts invalid country codes as well for CountByCountry actionType 

**Description:** API returns 200 OK status code while testing CountByGender actionType with invalid country code.

**Steps to reproduce:**
1. 	Send an HTTP Post request for ContByGender actionType with invalid country code.
2. 	Get the result including invalid country code values.
3. 	Observe the issue.

**Expected result:** Should return 400 Bad request for invalid country codes

**Actual result:** Returns 200 OK status code and counts invalid country codes as separate valid values
                                          
### Test case: test_count_by_empty_country_count

**Title:** Incorrect API response to the empty users' array

**Description:**
	When sending an empty users' array, the API should return a 400 - Bad Request [A syntax error in the client's request] status code. However, it returns 200 - OK status code.

**Steps to reproduce:**
1. 	Send an empty users' array POST request to the API.
2. 	Observe the issue.

**Expected result:** Should return 400 status code of Bad request

**Actual result:** Returns 200 OK status code

                                            
### Test case: test_count_by_country_missing_req_fields

**Title:** API returns 200 OK status code to the missing required field "nat"

**Description:** While testing CountByGender actionType with the missing required field API returns 200 OK status code with the count of null values.

**Steps to reproduce:**
1. 	Send an HTTP POST request with missing required "gender" fields to the API.
2. 	Get the result
3. 	Observe the issue.

**Expected result:** Should return 400 Bad request because of missing required fields

**Actual result:** Returns 200 OK status code with count of null values

### Test case: test_count_password_complexity_response_format

**Title:** API returns incorrect count of non-alphanumeric characters for the password complexity

**Description:** While testing CountPasswordComplexity actionType API returns incorrect comparison for the password complexity score.

**Steps to reproduce:**
1. 	Send an HTTP POST request with some low, medium and high score of password complexity
2. 	Get the result
3. 	Observe the issue.

**Expected result:** Should return the correct complexity score for the password

**Actual result:** Incorrect compare of the expected complexity score for the password

 
### Test case: test_valid_top_parameter_count_by_country

**Title:** API returns incorrect result of top parameter for CountByCountry actionType

**Description:** While executing test for valid top parameter CountByCountry's actionType, API returns correct and incorrect results. Some test executions were passed and some failed

**Steps to reproduce:**
1. 	Send an HTTP POST request with valid top parameter (in this case top is 3)
2. 	Get the result
3. 	Observe the issue.

**Expected result:** Should return correct result for valid top parameter

**Actual result:** Returned result greater than the top parameter. 

                                 
### Test case: test_negative_top_parameter_count_by_country 

**Title:** API response to the negative top parameter for CountByCountry actionType

**Description:**
	When sending an HTTP POST request with negative top parameter for the CountByCountry actionType it should return a 400 - Bad Request [A syntax error in the client's request] status code. However, it returns 200 - OK status code.

**Steps to reproduce:**
1. 	Send an HTTP POST request with negative top parameter to the API.
2. 	Observe the issue.

**Expected result:** Should return 400 status code of Bad request

**Actual result:** Returns 200 OK status code

                                    
### Test case: test_negative_top_parameter_count_by_gender

**Title:** API response to the negative top parameter for CountByGender actionType

**Description:**
	When sending an HTTP POST request with negative top parameter for the CountByGender actionType it should return a 400 - Bad Request [A syntax error in the client's request] status code. However, it returns 200 - OK status code.

**Steps to reproduce:**
1. 	Send an HTTP POST request with negative top parameter to the API.
2. 	Observe the issue.

**Expected result:** Should return 400 status code of Bad request

**Actual result:** Returns 200 OK status code 

                                     
### Test case: test_zero_top_parameter_count_by_gender 

**Title:** API response to the zero top parameter for CountByGender actionType

**Description:**
	When sending an HTTP POST request with top parameter equal to zero for the CountByGender actionType it should return a 400 - Bad Request [A syntax error in the client's request] status code. However, it returns 200 - OK status code.

**Steps to reproduce:**
1. 	Send an HTTP POST request with top parameter 0 to the API.
2. 	Observe the issue.

**Expected result:** Should return 400 status code of Bad request because top parameter should be greater than 0

**Actual result:** Returns 200 OK status code

                                          
### Test case: test_invalid_top_parameter_count_by_gender   

**Title:** API response to the invalid(non-integer) top parameter for CountByGender actionType

**Description:**
	When sending an HTTP POST request with invalid top parameter for the CountByGender actionType it should return a 400 - Bad Request [A syntax error in the client's request] status code. However, it returns 200 - OK status code.

**Steps to reproduce:**
1. 	Send an HTTP POST request with invalid(non-integer) top parameter to the API.
2. 	Observe the issue.

**Expected result:** Should return 400 status code of Bad request because top parameter should be an integer

**Actual result:** Returns 200 OK status code

                                      
### Test case: test_max_top_parameter_count_by_gender 

**Title:** API response to the maximum value of top parameter for CountByGender actionType

**Description:**
	When sending an HTTP POST request with max top parameter for the CountByGender actionType it should return a 400 - Bad Request [A syntax error in the client's request] status code. However, it returns 200 - OK status code.

**Steps to reproduce:**
1. 	Send an HTTP POST request with top parameter greater than available value to the API.
2. 	Observe the issue.

**Expected result:** Shouldn't accept the value greater than the max and should return 400 status code of Bad request

**Actual result:** Returns 200 OK status code to the given max top parameter
    
