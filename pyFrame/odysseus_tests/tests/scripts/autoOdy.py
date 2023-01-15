from odysseus_hub.WebDriverActions import WebDriverActions
from odysseus_hub.utils.ScreenGrabber import ScreenGrabber
from odysseus_modules.modules.B2BLoginSiteSelectionModule import *
from odysseus_modules.modules.SearchModule import SearchModule
from odysseus_hub.BaseTest import *
from odysseus_objects.PackageObject import PackageObject


class autoOdy(BaseTest):

    def __init__(self):
        self.b2BUsername = None
        self.b2BPassword = None
        self.parentSiid = None
        self.childSiid = None

        self.search_module = None
        self.b2bLoginModule = None
        self.packageObject = None

    def test(self):

        excelFile = "D:\\Work\\Git\\pyFrame_Shared\\pyFrame\\ScenarioSheet.xlsx"
        propertyFile = "D:\\Work\\Git\\pyFrame_Shared\\pyFrame\\odysseus_tests\\tests\\resources\\properties\\credentials.ini"
        urlFile = "D:\\Work\\Git\\pyFrame_Shared\\pyFrame\\odysseus_tests\\tests\\resources\\properties\\URLs.ini"
        screenShotPath = "D:\\Work\\Git\\pyFrame_Shared\\pyFrame\\odysseus_tests\\test_output\\full_page_screenshots"

        # Setup
        self.b2BUsername = self.getPropertyValue(propertyFile, "Username", "B2B_credentials")
        self.b2BPassword = self.getPropertyValue(propertyFile, "Password", "B2B_credentials")
        self.packageObject = PackageObject(excelFile)
        self.parentSiid = self.packageObject.getParentSiid()
        self.childSiid = self.packageObject.getChildSiid()
        self.setupB2CSiteURL(self.packageObject.getInstance(), "dpcpCruiseURL", urlFile)

        self.actions = WebDriverActions(self.packageObject.getBrowser())

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
        ScreenGrabber.getFullPageScreenshot(self.actions, screenShotPath, "searchPage_FullPageScreenshot")

        ScreenGrabber.getScreenshot(self.actions, screenShotPath, "Final_Screenshot")
        print("\n--------------Test Completed--------------")


autoOdy().test()
