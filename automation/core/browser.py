"""
Browser factory module.

This module provides a helper function for initializing and launching
a Playwright Chromium browser instance in asynchronous mode.
It is designed to be reused across automated UI tests and test runners.
"""

from playwright.async_api import async_playwright

async def create_browser(headless=True):
    """
    Create and launch a Chromium browser using Playwright.

    Args:
        headless (bool): Whether to run the browser in headless mode.
            Defaults to True.

    Returns:
        tuple: A tuple containing:
            - playwright: The initialized Playwright instance
            - browser: The launched Chromium browser instance
    """
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=headless)
    return playwright, browser
