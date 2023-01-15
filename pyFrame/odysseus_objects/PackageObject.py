from odysseus_hub.utils.ExcelUtils import ExcelUtils


class PackageObject:

    categoryPagePrice = None

    def __init__(self, excelPath):

        self.instance = ExcelUtils.getRowColData("G", "8", "ScenarioSheet", excelPath)
        self.product = ExcelUtils.getRowColData("G", "9", "ScenarioSheet", excelPath)
        self.sailingsDate = ExcelUtils.getRowColData("G", "10", "ScenarioSheet", excelPath)
        self.parentSiid = ExcelUtils.getRowColData("G", "11", "ScenarioSheet", excelPath)
        self.childSiid = ExcelUtils.getRowColData("G", "12", "ScenarioSheet", excelPath)
        self.browser = ExcelUtils.getRowColData("G", "13", "ScenarioSheet", excelPath)
        self.cruiseLine = ExcelUtils.getRowColData("G", "14", "ScenarioSheet", excelPath)
        self.scenario = ExcelUtils.getRowColData("G", "15", "ScenarioSheet", excelPath)

        self.finalResult = None
        self.ACN = None
        self.PNR = None

    def setCategoryPrice(self, category_price):
        self.categoryPagePrice = category_price

    def getCategoryPrice(self):
        return self.categoryPagePrice

    def setInstance(self, instance):
        self.instance = instance

    def getInstance(self):
        return self.instance

    def setProduct(self, product):
        self.product = product

    def getProduct(self):
        return self.product

    def setBrowser(self, browser):
        self.browser = browser

    def getBrowser(self):
        return self.browser

    def setSailingsDate(self, sailingsDate):
        self.sailingsDate = sailingsDate

    def getSailingsDate(self):
        return self.sailingsDate

    def setParentSiid(self, parentSiid):
        self.parentSiid = parentSiid

    def getParentSiid(self):
        return self.parentSiid

    def setChildSiid(self, childSiid):
        self.childSiid = childSiid

    def getChildSiid(self):
        return self.childSiid

    def setScenario(self, scenario):
        self.scenario = scenario

    def getScenario(self):
        return self.scenario

    def setFinalResult(self, finalResult):
        self.finalResult = finalResult

    def getFinalResult(self):
        return self.finalResult

    def setACN(self, ACN):
        self.ACN = ACN

    def getACN(self):
        return self.ACN

    def setPNR(self, PNR):
        self.PNR = PNR

    def getPNR(self):
        return self.PNR

    def setCruiseLine(self, cruiseLine):
        self.cruiseLine = cruiseLine

    def getCruiseLine(self):
        return self.cruiseLine

