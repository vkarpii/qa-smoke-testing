# QA Automation – Website Smoke Testing

This repository contains a simple smoke test automation setup for a Flask-based website.


## Project Structure

- `mock_site/` — Flask application that is being tested
- `automation/` — automated smoke tests


## Requirements

Before running the site and the tests, make sure you have the following installed:

- Python 3.10+
- Python packages:
  ```bash
  pip install flask playwright
  ```
- Playwright browsers:
  ```bash
  playwright install
  ```

## Running the mock site

1. Navigate to the `mock_site` directory:
   ```bash
   cd mock_site
   ```

2. Start the Flask application:
   ```bash
   python app.py
   ```

3. The site will be available at:
   ```
   http://127.0.0.1:5000
   ```

## Running the automated tests

⚠️ **Important:** the Flask mock site must be running before executing the tests.

1. Open a new terminal window.

2. Navigate to the `automation` directory:
   ```bash
   cd automation
   ```

3. Run the test runner:
   ```bash
   python run.py
   ```

The test runner will:
- Launch a headless browser
- Execute smoke tests against the running site
- Collect UI, console, and HTTP errors
- Generate an HTML test report
