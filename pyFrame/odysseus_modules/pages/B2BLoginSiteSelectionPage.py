from selenium.webdriver.common.by import By

from odysseus_hub.utils.StringUtils import StringUtils


class B2BLoginSiteSelectionPage:
    # Locators
    USER_NAME = By.ID, "UsernameTXT"
    PASSWORD = By.ID, "PasswordTXT"
    LOGIN_BTN = By.ID, "SubmitBTN"
    FORGOT_PASSWORD = By.ID, "RecoverPasswordBTN"

    SITE_SELECTION_PAGE_SELECT_SITE_LABEL = By.XPATH, "//div[@class='panel-heading']//h3[contains(text(),'Select Site')]"
    SITE_SELECTION_PAGE_SITE_LIST_TABLE = By.CSS_SELECTOR, "table.popuptable"
    siteSelectionPageEachTableRowXpath = "//tr[contains(@class,'rowValue')]"
    siteSelectionPageSiidSelectButtonXpath = siteSelectionPageEachTableRowXpath \
                                             + "//a[contains(@onclick,'siid={}') or contains(@href,'siid={}')][normalize-space(text())='Select']"

    # Constructor
    def __init__(self, actions, b2CSiteURL, parentSiid, childSiid, b2BUserName, b2BPassword):
        self.actions = actions
        self.parentSiid = parentSiid
        self.childSiid = childSiid
        self.b2BUserName = b2BUserName
        self.b2BPassword = b2BPassword

        self.domain = StringUtils.extractDomainFromURL(b2CSiteURL)
        self.b2bURL = "https://" + self.domain + ("/odyssey" if "odysolvd" in self.domain else "") + "/admin/login.aspx"

    # Methods
    def waitForSiteSelectionPageToLoad(self):
        self.actions.waitForElementToLoad(self.SITE_SELECTION_PAGE_SELECT_SITE_LABEL, 10,
                                          "Site label under site selection page")
        self.actions.waitForElementToLoad(self.SITE_SELECTION_PAGE_SITE_LIST_TABLE, 10,
                                          "Site List Table in site selection page")

    def login(self):
        if not self.isLoginFormDisplayed():
            self.actions.openUrl(self.b2bURL)
        self.fillLoginInfo()
        self.clickLoginBtn()
        self.actions.waitForDocumentToGetReady()

    def isLoginFormDisplayed(self):
        try:
            return (self.actions.isElementVisible(self.USER_NAME) and self.actions.isElementVisible(self.PASSWORD)
                    and self.actions.isElementVisible(self.FORGOT_PASSWORD) and self.actions.isElementVisible(
                        self.LOGIN_BTN))
        except Exception:
            return False

    def fillLoginInfo(self):
        self.actions.clearAndType(self.USER_NAME, self.b2BUserName)
        self.actions.clearAndType(self.PASSWORD, self.b2BPassword)

    def clickLoginBtn(self):
        self.actions.click(self.LOGIN_BTN)

    def clickSiidSelectBtn(self):
        selectSiteLocator = By.XPATH, self.siteSelectionPageSiidSelectButtonXpath.format(self.parentSiid,
                                                                                         self.parentSiid)
        onClickAttr = self.actions.getAttributeValue(selectSiteLocator, "onclick")
        if ("odysolvd" in StringUtils.extractDomainFromURL(self.b2bURL).lower()) and \
                not (StringUtils.extractDomainFromURL(self.b2bURL).toLowerCase() in onClickAttr.toLolowerwerCase()):
            existingHostName = StringUtils.extractValueFromPattern("selectSiteClickHandler\\('https:\\/\\/(.*)\\/\\/",
                                                                   onClickAttr)
            newOnclickAttrValue = onClickAttr.replace(existingHostName,
                                                      StringUtils.extractDomainFromURL(self.b2bURL)).replace("'", "\"")
            self.actions.getWebDriver().executeScript(
                "arguments[0].setAttribute('onclick','" + newOnclickAttrValue + "')",
                self.actions.getElement(selectSiteLocator))

        self.actions.click(selectSiteLocator)

    def isB2BLoginSuccessful(self):
        self.actions.waitForDocumentToGetReady()
        return not ("/login.aspx" in self.actions.getWebDriver().current_url)
