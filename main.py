
import logging

# debug
# info
# error
# warning
# critical

logging.basicConfig(filename='logger_detail.log', filemode='a', level=logging.DEBUG,
                        format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')

def sum(a,b):
    logging.info("started execution")
    c= a+b
    if c>12:
        print("greater than 12")
    elif c<12:
        print("less than 12")
        logging.error("value is less than 12")
    else:
        print("equal to 12")
        logging.warning("value is 12")
        logging.critical("Terminating program")
    return c


sum(5,7)



