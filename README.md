# weather-check
#### Video Demo: [URL HERE]
#### Description:

This project was done as the final project of the [Harvard CS50P](https://cs50.harvard.edu/python/2022/) course and meets the following requirements:
- The project must be implemented in Python.
- The project must have a main function and three or more additional functions. At least three of those additional functions must be accompanied by tests that can be executed with pytest.
- The main function must be in a file called "project.py," which should be in the root (i.e., top-level folder) of the project.
- Three required custom functions other than the main must also be in "project.py" and defined at the same indentation level as the main (i.e., not nested under any classes or functions).
- Test functions must be in a file called "test_project.py," which should also be in the root of the project. Make sure they have the same name as your custom functions, prepended with "test_" (e.g., "test_custom_function" where "custom_function" is a function you’ve implemented in "project.py").
- Optionally, implement additional classes and functions as fitting beyond the minimum requirement.
- Implementing the project should entail more time and effort than is required by each of the course’s problem sets.
- Pip-installable libraries that the project requires must be listed, one per line, in a file called "requirements.txt" in the root of your project.

*** 
The project is made to demonstrate the abilities of using:
- Functions and methods
- Different data types
- Loops and conditions
- Built-in libraries (argparse, csv, datetime, re, sys)
- Third-party libraries (geocoder, requests)
- Unit tests (pytest)
- File input/output
- Classes and subclasses
- Etc.
***
The project is a Python program that uses command-line arguments to print weather information for a certain location and forecast for tomorrow. Weather data include temperature and short descriptions (clouds/rain). Forecast data include tomorrow's maximal temperature and possibility of rain.

The absence of command-line arguments (default) prints the weather in metric units (celsius) in the current location (make sure not to use a VPN). The command-line argument `--location` allows you to get weather information in a specified location. The command-line argument `--units` allows you to get weather information in metric/imperial units (C/F).

Additionally, the program is logging all requests into a CSV file. The logged information includes:
- Total amount of requests
- Date and time of a request
- Amount of requests for today (the free OpenWeather API allows up to 1000 requests per day)
- String of a request
- Successful execution of the main function.
***
#### Files
- **project.py:** The main executive file
- **test_project.py:** Contains test functions
- **log.csv:** Contains data about requests

_PLEASE NOTE:_ The OpenWeather API is provided for test purposes. To obtain your own API key, register at [OpenWeather](https://openweathermap.org).
