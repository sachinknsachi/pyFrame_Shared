from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from odysseus_hub.WebDriverInstance import WebDriverInstance


class WebDriverActions(WebDriverInstance):

    def __init__(self, browser):
        super().__init__(browser)
        self.TIMEOUT = 30

    def getWebDriver(self):
        return self.webDriver

    # WebDriverWait actions
    def waitForElementToBePresent(self, locator):
        WebDriverWait(self.webDriver, 10).until(
            EC.presence_of_element_located((locator[0], locator[1])))

    def waitForElementToDisappear(self, locator):
        WebDriverWait(self.webDriver, 10).until(
            EC.invisibility_of_element_located((locator[0], locator[1])))

    def waitForDocumentToGetReady(self):
        WebDriverWait(self.webDriver, 60).until((lambda webDriver: webDriver
                                                 .execute_script("return document.readyState") == "complete"))

    def waitForElementToLoad(self, byLocator, timeOut, element):
        try:
            WebDriverWait(self.webDriver, timeOut).until(lambda webDriver: webDriver
                                                         .find_element(byLocator[0], byLocator[1]))
        except TimeoutException:
            raise TimeoutException(element.strip() + " is not loaded")

    def isElementDisplayed(self, byLocator, element, waitForElement=False):
        try:
            if waitForElement:
                self.waitForElementToLoad(byLocator, self.TIMEOUT, element)
            return self.webDriver.find_element(byLocator[0], byLocator[1]).is_displayed()
        except WebDriverException:
            return False

    # ActionChains actions
    def moveToElement(self, locator):
        ActionChains(self.webDriver).move_to_element(self.webDriver.find_element(locator[0], locator[1])).perform()

    # webDriver actions
    def waitForElementToBeVisible(self, locator):
        self.webDriver.find_element(locator[0], locator[1]).is_displayed()

    def click(self, locator, waitForElementToDisappear=False):
        self.waitForElementToBePresent(locator)
        self.waitForElementToBeVisible(locator)
        self.moveToElement(locator)
        self.webDriver.find_element(locator[0], locator[1]).click()
        if waitForElementToDisappear is True:
            self.waitForElementToDisappear(locator)

    def getTitle(self):
        return self.webDriver.title

    def type(self, locator, *text):
        self.waitForElementToBePresent(locator)
        self.waitForElementToBeVisible(locator)
        self.moveToElement(locator)
        self.webDriver.find_element(locator[0], locator[1]).send_keys(text)

    def clearAndType(self, locator, *text):
        self.waitForElementToBePresent(locator)
        self.waitForElementToBeVisible(locator)
        self.moveToElement(locator)
        self.webDriver.find_element(locator[0], locator[1]).clear()
        self.webDriver.find_element(locator[0], locator[1]).send_keys(text)

    def getAttributeValue(self, byLocator, attributeName):
        return self.webDriver.find_element(byLocator[0], byLocator[1]).get_attribute(attributeName)

    def getElement(self, byLocator):
        return self.webDriver.find_element(byLocator[0], byLocator[1])


