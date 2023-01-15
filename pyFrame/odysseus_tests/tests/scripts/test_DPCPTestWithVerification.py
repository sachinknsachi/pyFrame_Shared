from odysseus_hub.utils.ScreenGrabber import ScreenGrabber
from odysseus_modules.modules.B2BLoginSiteSelectionModule import *
from odysseus_modules.modules.SearchModule import SearchModule
from odysseus_hub.BaseTest import *
from odysseus_objects.PackageObject import PackageObject


class Test_DPCPTestWithVerification(BaseTest):

    def test_cruiseOnlyVerification(self, setup):

        # Setup
        self.b2BUsername = self.getPropertyValue("credentials", "Username", "B2B_credentials")
        self.b2BPassword = self.getPropertyValue("credentials", "Password", "B2B_credentials")

        excelPath = "D:\\Work\\Git\\pyFrame_Shared\\pyFrame\\ScenarioSheet.xlsx"
        self.packageObject = PackageObject(excelPath)

        self.parentSiid = self.packageObject.getParentSiid()
        self.childSiid = self.packageObject.getChildSiid()
        self.setupB2CSiteURL(self.packageObject.getInstance(), "dpcpCruiseURL")

        # creating objects
        self.b2bLoginModule = B2BLoginSiteSelectionModule(self.actions, self.getB2CSiteURL(), self.parentSiid,
                                                          self.childSiid, self.b2BUsername, self.b2BPassword)
        self.search_module = SearchModule(self.actions)

        # Opening browser and launching URL
        self.b2bLoginModule.loginAndOpenSite()
        self.actions.openUrl(self.getB2CSiteURL())

        # SearchPage Actions
        self.search_module.fillSearchData(self.packageObject)
        self.search_module.clickSearch()
        ScreenGrabber.getFullPageScreenshot(self.actions, "searchPage_FullPageScreenshot")


