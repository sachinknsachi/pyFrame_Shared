import configparser
import os

import pytest

from odysseus_hub.WebDriverActions import WebDriverActions
from odysseus_hub.utils.ScreenGrabber import ScreenGrabber


class BaseTest:

    config = None
    B2CURL = None
    actions = None

    @pytest.fixture()
    def setup(self):
        self.actions = WebDriverActions("Chrome")
        yield
        ScreenGrabber.getScreenshot(self.actions, "Final_Screenshot")
        print("\n--------------Test Completed--------------")

    def setupB2CSiteURL(self, instance, key, fileName="URLs"):
        self.B2CURL = self.getPropertyValue(fileName, key, instance)

    def getB2CSiteURL(self):
        return self.B2CURL

    def getPropertyValue(self, fileName, key, section="default"):
        self.config = configparser.RawConfigParser()
        file = os.path.abspath("./").split("odysseus_tests")[0] + "odysseus_tests\\tests\\resources\\properties\\" + fileName + ".ini"
        self.config.read(file)
        return self.config.get(section, key)


