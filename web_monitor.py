#!/usr/bin/python
"""web_monitor.py - Website monitoring tool

Runs requests and content checks on websites and reports them in various formats.

Configuration file: config.json

Without arguments runs the tests once, with a number argument runs the tests periodically.
"""

import sys
import json
from time import time, sleep

import keys

def usage():
    print 'Usage: {0} [monitor_interval (seconds)]'.format(sys.argv[0])

def main(argv):

    monitor_interval = 0
    config_filename = "config.json"
    config = None

    if len(argv) > 0:
        try:
            monitor_interval = int(argv[0])
        except ValueError:
            usage()
            sys.exit(0)

    with open(config_filename, "r") as f:
        config = json.load(f)

    if( config == None ):
        print "Failed to open " + config_filename
        sys.exit(0)


    while( True ):

        nextTime = time() + monitor_interval
        tester_key = config["tester"]
        logger_key = config["logger"]

        if( "logfile" in config ):
            logfile = config["logfile"]
        else:
            logfile = None

        logger = keys.objects[logger_key](logfile=logfile)
        test = keys.objects[ tester_key]( logger)

        for url in config["url_list"]:

            if( test.request(url)):
                test.content( config["url_list"][url] )
            logger.writeLog()

        endTime = time()
        if( monitor_interval <= 0 ):
            break;
        if( nextTime > endTime ):
            sleep(nextTime - endTime)


if __name__ == '__main__':
    main( sys.argv[1:])
