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

## Smoke Tests Coverage
The smoke test suite verifies:
- Page availability and basic navigation
- Presence of critical UI elements (header, navigation, main content)
- JavaScript console errors
- HTTP response status codes

## Tests expected to fail:
test_home_page_clicks → FAIL
 Error: 
 Link check failed: 'Go to About Page' -> http://localhost:3000/broken, reason: Broken link: 'Go to About Page' -> http://localhost:3000/broken, status 404

test_home_page_console_errors → FAIL
 Error: 
 JS console errors detected on /: ['Test JS error for smoke test']

## Extending the Tests
To add a new smoke test:
1. Create a new test file in automation/tests
2. Follow the existing async test structure
3. The test will be automatically discovered by the test runner