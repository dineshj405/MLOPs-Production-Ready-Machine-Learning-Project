from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys


logging.info("Demo file for MongoDB integration")   

try:
    a = 33/0
except Exception as e:  
    logging.info("Exception occurred")
    raise USvisaException(e, sys)