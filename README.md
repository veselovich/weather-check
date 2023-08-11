# weather-check
#### Video Demo:  <URL HERE>
#### Description:

This project was done as a final project of [Harvard CS50P](https://cs50.harvard.edu/python/2022/) course and meets following requirements:
- project must be implemented in Python.
- project must have a main function and three or more additional functions. At least three of those additional functions must be accompanied by tests that can be executed with pytest.
- main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of project.
- 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main (i.e., not nested under any classes or functions).
- test functions must be in a file called test_project.py, which should also be in the “root” of project. Be sure they have the same name as your custom functions, prepended with test_ (test_custom_function, for example, where custom_function is a function you’ve implemented in project.py).
- optional implementing additional classes and functions as fit beyond the minimum requirement.
- implementing project should entail more time and effort than is required by each of the course’s problem sets.
- pip-installable libraries that project requires must be listed, one per line, in a file called requirements.txt in the root of your project.
***
Porject is made to demonstrate abilities of using:
- functions, methods
- different data types
- loops and conditions
- built-in libraries (argparse, csv, datetime, re, sys)
- third party libraries (geocoder, requests)
- unit tests (pytest)
- file input/output
- classes and subclasses
- etc
***
Project is python program which uses command line arguments to print weather in certain location and forecast for tomorrow. Weather data include temperature and short description (clouds/rain). Forecast data include tomorrow's maximal temperatue and possibility of rain.

Absence of command line arguments (default) prints the weather in metrical units (celsius) in current location (make sure not to use VPN). Command line argument `--location` allows to get weather in specified location. Command line argument `--units` allows to get weather in metrical/imperial units (C/F).
In addition program logs all request into CSV-file.
Logged information:
- total amount of requests
- date and time of a request
- amount of requests for today (free OpenWeater API allows make up to 1000 request a day)
- string of a request
- successful executing of a main function
***
#### Files
- **project.py** - main executive file
- **test_project.py** - contains test functions
- **log.csv** - contains data about requests

_PLEASE NOTE:_ OpenWeather API is provided for test purposes. To obtain your own API register [OpenWeather](https://openweathermap.org).
