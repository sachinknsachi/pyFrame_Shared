from odysseus_modules.modules.B2BDefaultModule import B2BDefaultModule
from odysseus_modules.pages.B2BLoginSiteSelectionPage import B2BLoginSiteSelectionPage


class B2BLoginSiteSelectionModule(B2BLoginSiteSelectionPage):

    def __init__(self, actions, b2CSiteURL, parentSiid, childSiid, b2BUserName, b2BPassword):
        super().__init__(actions, b2CSiteURL, parentSiid, childSiid, b2BUserName, b2BPassword)
        self.childSiid = childSiid
        self.b2bDefaultModule = B2BDefaultModule(actions)
        self.b2BLoginSiteSelectionPage = B2BLoginSiteSelectionPage(actions, b2CSiteURL, parentSiid, childSiid,
                                                                   b2BUserName, b2BPassword)

    def waitForSiteSelectionPageToLoad(self):
        self.b2BLoginSiteSelectionPage.waitForSiteSelectionPageToLoad()

    def login(self):
        self.b2BLoginSiteSelectionPage.login()

    def isB2BLoginSuccessful(self):
        return self.b2BLoginSiteSelectionPage.isB2BLoginSuccessful()

    def clickSiidSelectBtn(self):
        self.b2BLoginSiteSelectionPage.clickSiidSelectBtn()

    def loginAndOpenSite(self):
        self.login()
        assert self.isB2BLoginSuccessful() == True
        self.waitForSiteSelectionPageToLoad()
        self.b2BLoginSiteSelectionPage.clickSiidSelectBtn()


