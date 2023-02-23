# nopApp_Framework

to genrate the html report

pytest -s -v --html=./Reports/login_report.html testCases/LoginTest.py
pytest -s -v --html=./Reports/customerRole_report.html testCases/AddCustomerRoleTest.py

GROUPPING :-
 pytest -s -v -m "sanity" --html=./Reports/new_report.html testCases/CustomerRoleTests.py --browser chrome
 pytest -s -v -m "regression" --html=./Reports/new_report.html testCases/CustomerRoleTests.py --browser chrome

Allure Report :-

pytest -s -v -m "sanity" --alluredir=/Users/testvagrant/PycharmProjects/nopApp/Reports/allureReport testCases/LoginTest.py --browser chrome

allure serve /Users/testvagrant/PycharmProjects/nopApp/Reports/allureReport

