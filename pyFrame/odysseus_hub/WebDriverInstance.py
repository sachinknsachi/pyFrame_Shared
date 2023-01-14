from selenium import webdriver


class WebDriverInstance:

    def __init__(self, browser):
        self.webDriver = None
        self.browser = browser

    def getWebDriver(self):
        return self.webDriver

    def openUrl(self, URL):
        assert URL is not None
        if self.webDriver is None and self.browser == "Chrome":
            self.webDriver = webdriver.Chrome()
        elif self.webDriver is None and self.browser == "Firefox":
            self.webDriver = webdriver.Firefox()
        elif self.webDriver is None and self.browser == "Ie":
            self.webDriver = webdriver.Ie()
        self.webDriver.get(URL)
        self.webDriver.implicitly_wait(10)
        self.webDriver.maximize_window()

