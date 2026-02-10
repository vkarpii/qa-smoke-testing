"""
Test reporting module.

This module provides a Reporter class responsible for presenting
test execution results in multiple formats:
    - Console output
    - JSON report
    - HTML report

It is designed to be used in lightweight QA automation frameworks,
such as smoke or regression test runners.
"""

import os
import json
from datetime import datetime

class Reporter:
    """
    Test results reporter.

    Attributes:
        results (list): List of test result dictionaries.
        json_folder (str): Directory where JSON reports are stored.
        html_folder (str): Directory where HTML reports are stored.
    """
    
    def __init__(self, results, json_folder="report_json", html_folder="report_html"):
        """
        Initialize the Reporter.

        Args:
            results (list): List of test result dictionaries.
                Each result is expected to have the following keys:
                - 'test': Test name
                - 'status': Test execution status (PASS / FAIL)
                - 'error' (optional): Error message if the test failed
            json_folder (str): Folder for JSON reports.
            html_folder (str): Folder for HTML reports.
        """
        
        self.results = results
        self.json_folder = json_folder
        self.html_folder = html_folder
        
        os.makedirs(self.json_folder, exist_ok=True)
        os.makedirs(self.html_folder, exist_ok=True)
        
        
    def print_console(self):
        """
        Print a human-readable test report to the console.

        Displays test names, statuses, and error messages (if present)
        in a simple and readable format.
        """
        print("\nTEST REPORT")
        print("=" * 40)
        for result in self.results:
            print(f"{result['test']} → {result['status']}")
            if result.get("errorMessage"):
                print(f"   Error: {result['errorMessage']}")   
                
    def to_json(self):
        """
        Export test results to a JSON file.

        The report file is saved with a timestamp-based filename
        inside the configured JSON reports directory.

        Returns:
            str: Path to the generated JSON report file.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join(self.json_folder, f"report_{timestamp}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.results, f, ensure_ascii=False, indent=4)
        print(f"[INFO] JSON report saved to {path}")
        return path
    
    def to_html(self):
        """
        Export test results to an HTML report.

        Generates an HTML report using a predefined template and
        dynamically injects test result data into the table.

        Returns:
            str: Path to the generated HTML report file.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join(self.html_folder, f"report_{timestamp}.html")

        template_path = os.path.join(os.path.dirname(__file__), "templates", "report_template.html")

        with open(template_path, "r", encoding="utf-8") as f:
            template = f.read()

        table_rows = ""
        for result in self.results:
            status_class = "pass" if result["status"].lower() == "pass" else "fail"
            error_text = result.get("errorMessage", "")
            table_rows += f"""
            <tr class="{status_class}">
                <td>{result['test']}</td>
                <td>{result['status']}</td>
                <td>{error_text}</td>
            </tr>
            """
        html_content = template.replace("{{timestamp}}", timestamp).replace("{{table_rows}}", table_rows)


        with open(path, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"[INFO] HTML report saved to {path}")
        return path