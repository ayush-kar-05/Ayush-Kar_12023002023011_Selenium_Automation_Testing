# Capstone 2 – Selenium Python Automation Framework

A modular **Selenium Python Automation Framework** for testing an e-commerce application using **PyTest, Unittest, Page Object Model (POM), CSV test data, configuration management, screenshots, and HTML reporting**.

## 🚀 Features

* Selenium WebDriver automation
* PyTest and Unittest support
* Page Object Model (POM)
* CSV-based test data handling
* Configuration management using `config.ini`
* Reusable PyTest fixtures
* Screenshot capture for failures
* HTML test reporting
* Modular and maintainable framework structure

## 🛠️ Tech Stack

* **Python**
* **Selenium WebDriver**
* **PyTest**
* **Unittest**
* **CSV**
* **ConfigParser**
* **PyTest HTML**
* **Chrome WebDriver**
* **Git & GitHub**

## 📁 Project Structure

```text
Capstone2_Selenium_Framework/
│
├── config/
│   └── config.ini
│
├── Pages/
│   ├── home_page.py
│   ├── login_page.py
│   ├── product_page.py
│   └── cart_page.py
│
├── Utilities/
│   ├── csv_reader.py
│   ├── config_reader.py
│   └── screenshot.py
│
├── test_data/
│   └── test_data.csv
│
├── tests/
│   ├── test_login.py
│   ├── test_search.py
│   └── test_cart.py
│
├── unittest_test/
│   └── test_login_unittest.py
│
├── screenshots/
├── reports/
├── venv/
│
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## 🧩 Framework Components

### Page Object Model

The `Pages/` directory contains page classes that handle locators and page-specific actions. This keeps test logic separate from UI interaction logic and improves maintainability.

### Utilities

The `Utilities/` directory provides reusable functions for:

* Reading CSV test data
* Reading configuration values
* Capturing screenshots

### Test Data

Test inputs are maintained separately in:

```text
test_data/test_data.csv
```

This supports data-driven testing without hardcoding test data inside test cases.

### Configuration

Application settings such as the application URL and browser are maintained in:

```text
config/config.ini
```

and accessed through `config_reader.py`.

## 🧪 Automated Test Scenarios

The framework currently covers:

1. **Login Testing**
2. **Product Search**
3. **Product Selection**
4. **Add Product to Cart**
5. **Cart Verification**

Both **PyTest** and **Unittest** implementations are included.

## ⚙️ Setup

Clone the repository:

```bash
git clone <your-repository-url>
cd Capstone2_Selenium_Framework
```

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run Tests

Run all PyTest tests:

```bash
pytest
```

Run individual tests:

```bash
pytest tests/test_login.py
pytest tests/test_search.py
pytest tests/test_cart.py
```

Run the Unittest test:

```bash
python -m unittest unittest_test.test_login_unittest
```

## 📊 HTML Report

Generate an HTML test report using:

```bash
pytest --html=reports/report.html --self-contained-html
```

The report will be generated inside:

```text
reports/
```

## 📸 Screenshots

Failure screenshots are stored in:

```text
screenshots/
```

They help in debugging failed test cases by capturing the browser state at the time of failure.

## 🔄 Framework Flow

```text
Test Cases
    ↓
Page Objects
    ↓
Selenium WebDriver
    ↓
E-Commerce Application
```

Supporting components:

```text
CSV Data ───────→ Tests
Config File ────→ Framework
Screenshot ─────→ Failure Evidence
HTML Report ────→ Test Results
```

## 🔮 Future Enhancements

* Cross-browser testing
* Parallel execution
* Logging
* CI/CD integration
* Selenium Grid
* Allure reporting

## 👩‍💻 Author

**Ayush Kar**
B.Tech – Computer Science & Engineering
Institute of Engineering and Management, Kolkata

**Project:** Selenium Python Automation Framework
**Type:** Academic Capstone Project