"""Test classes and functions for website requests and content checks.

Classes handle sending the requests and running the required functions on
the website response content.


"""

import requests
from requests import exceptions
import keys


class GetTest():
    """ Simple get request to url

    Args:
        log: Object with logResponse and logContent methods
        timeout (Optional[float]): Timeout value for request


    Attributes:
        log: Object for logging the results
        timeout (float): Timeout value for get request
        response: The response object created after request

    """

    def __init__(self, log, timeout=9.05):
        self.log = log
        self.timeout = timeout
        self.response = None


    def request(self, url):
        """Runs a get request and saves the response object

        Calls the logging method

        Returns:
            True if returned html code indicates success

        """
        success = True

        try:
            self.response = requests.get(url, timeout=self.timeout)
            status = self.response.status_code
            elapsed = self.response.elapsed.total_seconds()

        except requests.exceptions.RequestException as err:
            status = err.__class__.__name__
            elapsed = ""
            success = False

        self.log.logResponse(url, status, elapsed)
        return success




    def content(self, test_dict ):
        """Runs tests on the returned content

        Args:
            Config dictionary: { "function key" : [ arg1, arg2 ... ] }

        Returns:
            True if all content tests were successfull
        """

        success = True
        for func_key in test_dict:
            for arg in test_dict[func_key]:
                success = keys.objects[func_key](self.response, arg)
                if( not success): break
        self.log.logContent( success )
        return success



def needleInHay(response, needle ):
    return needle.lower() in response.text.lower()

def caseSensitiveNeedleInHay(response, needle ):
    return needle in response.text
