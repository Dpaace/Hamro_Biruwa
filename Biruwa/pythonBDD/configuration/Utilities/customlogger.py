import logging
import logging.handlers
from asyncio.log import logger
from stat import filemode


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="pythonBDD/configuration/Logs/yourApplog.log", format='%(asctime)s -%(message)s',
        datefmt='%d-%b-%y %H:%M:%S', filemode='w')
        rotate_file = logging.handlers.RotatingFileHandler(
           "pythonBDD/configuration/Logs/yourApplog.log", maxBytes=1024 * 1024 * 20, backupCount=3

        )
        logger= logging.getLogger()
        logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        return logger
        

