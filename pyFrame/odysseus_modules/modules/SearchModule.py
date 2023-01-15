from odysseus_modules.pages.SearchPage import SearchPage


class SearchModule:

    def __init__(self, actions):
        self.actions = actions
        self.search_page = SearchPage(self.actions)

    def waitForPageToLoad(self):
        self.search_page.waitForPageToLoad()

    def selectCruiseLine(self, cruiseLine):
        self.search_page.selectCruiseLine(cruiseLine)

    def fillSearchData(self, packageObject):
        self.search_page.fillSearchData(packageObject)

    def clickSearch(self):
        self.search_page.clickSearch()
