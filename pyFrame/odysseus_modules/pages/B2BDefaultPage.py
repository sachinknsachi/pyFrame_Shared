from selenium.webdriver.common.by import By


class B2BDefaultPage:
    # Locations
    affiliateNameLocator = "//ul[contains(@id,'select2Extended-results')]"
    AFFILIATE_NAME_INPUT = By.CSS_SELECTOR, "div.select2Extended-search > input#s2id_autogen1_search"
    ADMIN_AFF_DROPDOWN = By.CSS_SELECTOR, "span.select2Extended-chosen"

    def __init__(self, actions):
        self.actions = actions
        self.affiliateSelector = None

    def selectAffiliate(self, affiliateID):
        if self.actions.isElementDisplayed(self.ADMIN_AFF_DROPDOWN, "Admin affiliate drop down", True):
            self.actions.click(self.ADMIN_AFF_DROPDOWN)
        self.actions.type(self.AFFILIATE_NAME_INPUT, affiliateID)
        self.affiliateSelector = By.XPATH, self.affiliateNameLocator + "//li[contains(.,'" + affiliateID + "')]"
        self.actions.waitForElementToBeVisible(self.affiliateSelector)
        self.actions.click(self.affiliateSelector)




