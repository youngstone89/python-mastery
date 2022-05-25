import logging 
import os

filepath = os.path.abspath(__file__)
dirname = os.path.dirname(filepath)
logFilePath = os.path.join(dirname,'example.log')
logging.basicConfig(filename=logFilePath, level=logging.DEBUG)
logging.warning('watch out')
logging.info('i told you so')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')