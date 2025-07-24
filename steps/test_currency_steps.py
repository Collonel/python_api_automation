import requests
from pytest_bdd import scenarios, given, when, then
import pytest

BASE_URL = "https://restcountries.com/v3.1/currency/"

scenarios('../features/test_currency.feature')

@pytest.fixture
def context():
    return {}

@given('I have a valid currency code "KES"')
def valid_currency(context):
    context['currency'] = 'KES'

@given('I have an invalid currency code "XYZ"')
def invalid_currency(context):
    context['currency'] = 'XYZ'

@when('I send a request to the API')
def send_request(context):
    currency = context['currency']
    response = requests.get(f"{BASE_URL}{currency}")
    context['response'] = response

@then('the response status code should be 200')
def check_status_code(context):
    assert context['response'].status_code == 200

@then('I should get at least one country name in the response')
def check_country_name(context):
    data = context['response'].json()
    assert isinstance(data, list)
    assert 'name' in data[0]
    assert 'common' in data[0]['name']

@then('the response status code should not be 200')
def check_error_status_code(context):
    assert context['response'].status_code != 200

@then('I should get an error message or empty response')
def check_error_message(context):
    try:
        data = context['response'].json()
        assert isinstance(data, dict) or data == [] or data == {}
    except Exception:
        assert context['response'].text == ""
