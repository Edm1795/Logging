import logging

logging.basicConfig(format='%(funcName)s %(asctime)s - %(message)s', datefmt='%b-%d-%y %H:%M:%S') # only keep this for testing
# basicConfig(format='%(process)d-%(levelname)s-%(message)s') # Use this to include the level of the message

# Configure the logger (only call this once at outset of program, further calls will have no effect; filemode default is 'a' (append)
logging.basicConfig(level=logging.DEBUG,filename='practice.log', filemode='w', format='%(funcName)s %(asctime)s -  %(message)s',  datefmt='%d-%b-%y %H:%M:%S')




def go():

    logging.debug('This will get logged')
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

go()
