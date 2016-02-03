"""Logging classes for website monitoring

This module contains the classes for logging the website responses.
Should be developed with the testers in mind, as the tester classes will call
these directly.

"""
from time import strftime


class PrintLog():


    def __init__(self, delimiter=" "):
        self.timeformat = "%x" + delimiter + "%X"
        self.delimiter = delimiter
        self.logline = ""

    def logResponse(self, url, status, elapsed):
        self.logline = "{1}{0}{2}{0}{3}{0}{4}".format(self.delimiter,
                        strftime(self.timeformat), url, status,
                        elapsed if elapsed else "")

    def logContent(self, status):
        self.logline = "{1}{0}content:{2}".format( self.delimiter, self.logline,
                        "Pass" if status else "Fail")

    def writeLog(self):
        print self.logline
        self.logline = ""


class FileLog(PrintLog):

    def __init__(self, delimiter=" ", logfile=None):
        PrintLog.__init__(self, delimiter)

        if( logfile == None):
            self.logfile = strftime('monitor_%d_%m_%Y.log')
        else:
            self.logfile = logfile

    def writeLog(self):
        with open(self.logfile, 'a') as f:
            f.write(self.logline + "\n")
        self.logline = ""
