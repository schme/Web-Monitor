# A website monitoring tool

Periodically connects to listed websites and compares the fetched page to given test cases (eg. matching strings), reporting the result to a file or stdout. Designed with ease of extension and modularity in mind.

## Installation

Python2.7

Requests library for connection handling:
    `pip install requests`
For more information: http://docs.python-requests.org/en/latest/

## Configuration

When making your own configuration file consult keys.py for available functions and their
corresponding string keys.

A logfile can be specified in config.json with a "logfile" key-value pair. If no logfile is specified and file logging is on, a dated custom file is used.
