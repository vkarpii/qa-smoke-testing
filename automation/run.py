"""
Test runner entry point.

This module serves as the main entry point for the QA automation framework.
It is responsible for:
    - Loading runtime configuration
    - Discovering test cases
    - Executing tests asynchronously
    - Generating test execution reports
"""

import asyncio
import json

from core.runner import run_tests
from core.reporter import Reporter
from core.collect_tests import collect_tests

tests_folder = "tests"

with open("config/config.json") as f:
    config = json.load(f)

async def main():
    """
    Main asynchronous test execution flow.

    This function performs the following steps:
        1. Collect test functions from the tests directory
        2. Execute collected tests using the test runner
        3. Generate console, JSON, and HTML reports
    """
    tests = collect_tests(tests_folder)

    results = await run_tests(tests, config)
    
    reporter = Reporter(results)
    reporter.print_console()
    reporter.to_json()
    reporter.to_html()

asyncio.run(main())
