"""Key: object pairings used in most of the program.

These keys are used in configuration files and the program uses this module
to pair them to certain objects, functions and classes.

Should be consulted when making and editing the configuration file.


get: a simple get request to the assigned url

print_log: print to stdout
file_log: create a logfile and print it there

string_search: a non-case sensitive search from the response text
string_search_case: a case-sensitive string_search
"""


import testers
import loggers

objects = {
    "get" : testers.GetTest,

    "print_log" : loggers.PrintLog,
    "file_log" : loggers.FileLog,

    "string_search" : testers.needleInHay,
    "string_search_case" : testers.caseSensitiveNeedleInHay,
}

