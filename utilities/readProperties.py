import configparser

config = configparser.RawConfigParser()
config.read("/Users/testvagrant/PycharmProjects/nopApp/Configurations/config.ini")


class ReadConfigFile:

    def getBaseUrl(self):
        return config.get('common-info', 'baseURL')

    def getUsername(self):
        return config.get('common-info', 'username')

    def getPassword(self):
        return config.get('common-info', 'password')
