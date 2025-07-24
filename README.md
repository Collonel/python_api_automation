This project automates BDD-style API tests against the public RestCountries API using Python, pytest-bdd, and the requests library. It includes:
- Two test scenarios (happy + unhappy paths)
- Pytest-BDD for BDD-style testing
- Requests for HTTP interaction
- HTML reporting using pytest-html

API Endpoint Under Test
https://restcountries.com/v3.1/currency/{currency}

```
api_automation/
│
├── features/
│   ├── test_currency.feature       # BDD feature file
│   └── steps/
│       └── test_currency_steps.py  # Step definitions
│
├── tests/
│   └── test_runner.py              # (optional)
│
├── reports/
│   └── api_test_report.html        # HTML test report (generated)
│
├── requirements.txt                # Project dependencies
├── conftest.py                     # Shared fixtures/context
└── README.md                       # Project guide
```
 
Prerequisites
- Python 3.11.1
- PyCharm or any modern Python IDE
- Internet access (tests hit a public API)

How to Set Up and Run
git clone
cd restcountries-api-test
Create a virtual environment
- python -m venv venv
- venv\Scripts\activate

Install dependencies
- pip install -r requirements.txt

Run the Tests
- pytest -v

Generate Report
- pytest -v --html=reports/api_test_report.html --self-contained-html


Happy Testing! 🚀