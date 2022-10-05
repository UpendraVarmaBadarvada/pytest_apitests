# test cases and classes should start with test
# pytest -s -v folder_name:- -s displays print statement and -v displays test case name with status
# pytest -s -v -k method_name folder_name:- execute a specific test case in a folder
# pytest -s -v -m tag_name folder_name:- executed tagged test cases
# pytest -s -v -m "not tag_name" folder_name:- execute all except tagged test cases
# pytest -s -v -m "tag1_name or tag2_name" folder_name:- execute tag1 or tag2 tc's
# pytest -s -v -m "tag1_name and tag2_name" folder_name:- execute tc's with tag1 and tag2
# we have registered these tags in the below ini file
# we can generate html report using below command
# pytest ApiTestCases --html-report=./ApiTestCases/api_testcases_report.html
# pytest --alluredir ./Reports ApiTestCases :- generates allure reports in json
# allure serve json_reports_dir_path to serve the allure reports


import pytest

# we use mark for tagging with custom name


@pytest.mark.regression
def test_method():
    print("this is a pytest regression test method")


@pytest.mark.smoke
def test_smoke_basic():
    print("this is a smoke test")


@pytest.mark.sanity
def test_sanity_basic():
    print("this is a sanity test")
