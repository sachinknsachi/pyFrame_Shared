from odysseus_hub.utils.ScreenGrabber import ScreenGrabber
from odysseus_modules.modules.B2BLoginSiteSelectionModule import *
from odysseus_modules.modules.SearchModule import SearchModule
from odysseus_hub.BaseTest import *


class Test_DPCPTestWithVerification(BaseTest):

    instance = "UAT"

    def test_cruiseOnlyVerification(self, setup):

        self.b2BUsername = self.getPropertyValue("credentials", "Username", "B2B_credentials")
        self.b2BPassword = self.getPropertyValue("credentials", "Password", "B2B_credentials")

        if self.instance == "UAT":
            self.parentSiid = 130386
            self.childSiid = 130386
        self.setupB2CSiteURL(self.instance, "dpcpCruiseURL")

        # creating objects
        self.b2bLoginModule = B2BLoginSiteSelectionModule(self.actions, self.getB2CSiteURL(), self.parentSiid,
                                                          self.childSiid, self.b2BUsername, self.b2BPassword)
        self.search_module = SearchModule(self.actions)

        # Opening browser and launching URL
        self.b2bLoginModule.loginAndOpenSite()
        self.actions.openUrl(self.getB2CSiteURL())

        # SearchPage Actions
        self.search_module.fillSearchData("August", 10, 20, "Royal Caribbean")
        self.search_module.clickSearch()
        ScreenGrabber.getFullPageScreenshot(self.actions, "searchPage_FullPageScreenshot")


