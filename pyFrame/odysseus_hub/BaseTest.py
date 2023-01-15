import configparser
import os


class BaseTest:

    config = None
    B2CURL = None
    actions = None

    def setupB2CSiteURL(self, instance, key, fileName="URLs"):
        self.B2CURL = self.getPropertyValue(fileName, key, instance)

    def getB2CSiteURL(self):
        return self.B2CURL

    def getPropertyValue(self, file, key, section="default"):
        self.config = configparser.RawConfigParser()
        self.config.read(file)
        return self.config.get(section, key)


