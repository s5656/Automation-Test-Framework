import logging


class LogGenrator:
    @staticmethod
    def logFileGenrator1():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format="%(asctime)s: %(levelname)s: %(message)s",  datefmt="%m/%d/%Y %I:%M:%S %p")

        logger = logging.getLogger()  # create object of logger and return info/debug lavels
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def logFileGenrator():
        logging.basicConfig(filename="/Users/testvagrant/PycharmProjects/nopApp/Logs/automation.log",
                            level=logging.INFO,
                            format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

        logger = logging.getLogger()    # create object of logger and return info/debug lavels
        logger.setLevel(logging.INFO)
        return logger
