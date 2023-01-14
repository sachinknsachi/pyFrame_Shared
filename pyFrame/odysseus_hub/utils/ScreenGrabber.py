import os

from selenium.webdriver.common.by import By


class ScreenGrabber:

    @staticmethod
    def getFullPageScreenshot(actions, screen_shot_name):
        s = lambda x: actions.getWebDriver().execute_script('return document.body.parentNode.scroll' + x)
        actions.getWebDriver().set_window_size(s('Width'), s('Height'))
        filePath = os.path.abspath("./").split("odysseus_tests")[0]\
                   + "odysseus_tests\\test_output\\full_page_screenshots\\" + screen_shot_name + ".png"
        actions.getWebDriver().find_element(By.TAG_NAME, 'body').screenshot(filePath)

    @staticmethod
    def getScreenshot(actions, screen_shot_name):
        filePath = os.path.abspath("./").split("odysseus_tests")[0]\
                   + "odysseus_tests\\test_output\\full_page_screenshots\\" + screen_shot_name + ".png"
        actions.getWebDriver().save_screenshot(filePath)

