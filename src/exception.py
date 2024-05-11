# for the exception handling

# for writing the exception handling code, all you have to do is basically search google for exception handling in python first
# "exception python documentation" is what you have to search first

# or you can write your own custom execption.


# writing our own custom exceptions : 

import sys
import logging
# sys library provides for any exception that python throws at you.
# we create a execption handling/ error handling function in python that is based off of sys.


def error_message_details(error, error_detail :sys):
    # the way sys gives out the information is interesting. You only need the last part of the output:

    _,_,exc_tb = error_detail.exc_info() # we dont need the first two infos. Just the third.
    file_name = exc_tb.tb_frame.f_code.co_filename  # this is basically a long procedure to get the file_name
    error_message ="Error occured in python script name[{0}] line number [{1}] error message[{2}]".format()
    file_name,exc_tb.tb_lineno,str(error)
    return error_message


class CustomException(Exception):
    def __init__(self,error_message, error_detail :sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message