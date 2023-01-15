from selenium.webdriver.common.by import By


class ScreenGrabber:

    @staticmethod
    def getFullPageScreenshot(actions, folder, screen_shot_name):
        s = lambda x: actions.getWebDriver().execute_script('return document.body.parentNode.scroll' + x)
        actions.getWebDriver().set_window_size(s('Width'), s('Height'))
        filePath = folder + screen_shot_name + ".png"
        actions.getWebDriver().find_element(By.TAG_NAME, 'body').screenshot(filePath)

    @staticmethod
    def getScreenshot(actions, folder, screen_shot_name):
        filePath = folder + screen_shot_name + ".png"
        actions.getWebDriver().save_screenshot(filePath)

