
import os
import importlib
import inspect

def collect_tests(tests_folder):
   
    tests = []

    for filename in os.listdir(tests_folder):
        if filename.startswith("test_") and filename.endswith(".py"):
            module_name = f"{tests_folder}.{filename[:-3]}"
            module = importlib.import_module(module_name)

            for name, obj in inspect.getmembers(module):
                if inspect.iscoroutinefunction(obj) and name.startswith("test_"):
                    tests.append(obj)

    return tests