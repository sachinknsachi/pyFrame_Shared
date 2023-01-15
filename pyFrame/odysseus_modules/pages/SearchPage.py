from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class SearchPage:
    # Sailing "By" locators
    LOADER = By.XPATH, "//div[@class='loader']"
    LOADER_BUBBLE = By.XPATH, "//span[@class='loader-bubble']"
    LOADER_SPIRAL = By.XPATH, "//div[@class='loader-spiral']"
    SAILINGS_DATES_LOCATOR = By.XPATH, "//input[@data-ody-id='sailingDates']"
    SAILINGS_DATES_CALENDER_HEADER_YEAR = By.XPATH, "(//button[@class='current'])[1]"
    SAILINGS_DATES_CALENDER_HEADER_MONTH = By.XPATH, "(//button[@class='current ng-star-inserted'])[1]"
    SAILINGS_DATES_CALENDER_NEXT_BUTTON = By.XPATH, "//button[@class='next' and @style='visibility: visible;']"
    SAILINGS_DATES_CALENDER_PREVIOUS_BUTTON = By.XPATH, "//button[@class='previous' and @style='visibility: visible;']"

    # Sailing "String" locators
    SAILINGS_DATES_CALENDER_DAY = "(//div[@class='bs-datepicker-body'])[1]//td//span[text()='{}' and not(@class='is-other-month')]"
    SAILINGS_DATES_CALENDER_YEAR = "//table[@class='years']//span[text()='{}']"
    SAILINGS_DATES_CALENDER_MONTH = "(//table[@class='months']//span[text()='{}'])[1]"

    # Select CruiseLine Locators
    CRUISE_LINE_SELECTOR = By.CSS_SELECTOR, "ody-dropdown[data-ody-id='cruiselines'] input"

    # Search Button
    SEARCH_BUTTON = By.CSS_SELECTOR, "button[data-ody-id='SearchButton']"

    def __init__(self, actions):
        self.actions = actions

    def waitForPageToLoad(self):
        self.actions.waitForElementToDisappear(self.LOADER_SPIRAL)
        self.actions.waitForElementToDisappear(self.LOADER)
        self.actions.waitForElementToDisappear(self.LOADER_BUBBLE)

    def selectSailings(self, packageObject):
        self.actions.waitForElementToDisappear(self.LOADER_SPIRAL)
        self.actions.waitForElementToDisappear(self.LOADER)
        self.actions.waitForElementToDisappear(self.LOADER_BUBBLE)

        self.actions.click(self.SAILINGS_DATES_LOCATOR)
        self.actions.click(self.SAILINGS_DATES_CALENDER_HEADER_YEAR)
        sailings = packageObject.getSailingsDate()
        self.actions.click([By.XPATH, self.SAILINGS_DATES_CALENDER_YEAR.format(sailings.year)])
        self.actions.click([By.XPATH, self.SAILINGS_DATES_CALENDER_MONTH.format(sailings.strftime('%B'))])
        self.actions.click([By.XPATH, self.SAILINGS_DATES_CALENDER_DAY.format(sailings.day)])
        self.actions.click([By.XPATH, self.SAILINGS_DATES_CALENDER_DAY.format(sailings.day + 10)])

        self.actions.waitForElementToDisappear(self.LOADER_SPIRAL)
        self.actions.waitForElementToDisappear(self.LOADER)
        self.actions.waitForElementToDisappear(self.LOADER_BUBBLE)

    def selectCruiseLine(self, packageObject):
        self.actions.waitForElementToDisappear(self.LOADER_SPIRAL)
        self.actions.waitForElementToDisappear(self.LOADER)
        self.actions.waitForElementToDisappear(self.LOADER_BUBBLE)

        self.actions.type(self.CRUISE_LINE_SELECTOR, packageObject.getCruiseLine())
        self.actions.type(self.CRUISE_LINE_SELECTOR, Keys.ENTER)

        self.actions.waitForElementToDisappear(self.LOADER_SPIRAL)
        self.actions.waitForElementToDisappear(self.LOADER)
        self.actions.waitForElementToDisappear(self.LOADER_BUBBLE)

    def clickSearch(self):
        self.actions.waitForElementToDisappear(self.LOADER_SPIRAL)
        self.actions.waitForElementToDisappear(self.LOADER)
        self.actions.waitForElementToDisappear(self.LOADER_BUBBLE)

        self.actions.click(self.SEARCH_BUTTON)

        self.actions.waitForElementToDisappear(self.LOADER_SPIRAL)
        self.actions.waitForElementToDisappear(self.LOADER)
        self.actions.waitForElementToDisappear(self.LOADER_BUBBLE)

    def fillSearchData(self, packageObject):
        self.waitForPageToLoad()
        self.selectSailings(packageObject)
        self.actions.waitForElementToDisappear(self.LOADER_SPIRAL)
        self.actions.waitForElementToDisappear(self.LOADER)
        self.actions.waitForElementToDisappear(self.LOADER_BUBBLE)
        self.selectCruiseLine(packageObject)

