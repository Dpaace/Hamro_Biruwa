import configparser
from distutils.command.config import config
config=configparser.RawConfigParser()
config.read(".\\pythonBDD\\configuration\\config.ini")

class ReadConfig:
    @staticmethod

    def getURL():
        url =config.get('common-info', 'baseURL')
        return url


    @staticmethod
    def getUserName():
        username=config.get('common-info','userName') 
        return username  


    @staticmethod
    def getPassword():
        password=config.get('common-info','passWord')  
        return password  