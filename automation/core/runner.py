"""
Test execution module.

This module provides the main asynchronous test runner responsible for:
    - Initializing the browser environment
    - Executing collected test cases
    - Handling test failures and exceptions
    - Aggregating test execution results
"""

from core.browser import create_browser

async def run_tests(tests, config):
    """
    Execute a list of asynchronous tests.

    This function initializes a browser instance, runs each test
    sequentially, captures execution results, and ensures that
    all browser resources are properly cleaned up after execution.

    Each test is expected to be an async function with the following signature:
        async def test_name(page, config)

    Args:
        tests (list): List of asynchronous test functions to execute.
        config (dict): Configuration dictionary containing runtime settings.
            Expected keys:
                - headless (bool): Whether to run the browser in headless mode.

    Returns:
        list: List of test result dictionaries.
            Each result contains:
                - 'test': Test function name
                - 'status': PASS or FAIL
                - 'error' (optional): Error message if the test failed
    """
    playwright, browser = await create_browser(config["headless"])
    page = await browser.new_page()

    results = []

    for test in tests:
        try:
            await test(page, config)
            results.append({
                "test": test.__name__,
                "status": "PASS"
            })
        except Exception as e:
            results.append({
                "test": test.__name__,
                "status": "FAIL",
                "errorMessage": str(e)
            })

    await browser.close()
    await playwright.stop()

    return results
