from odysseus_modules.pages.SearchPage import SearchPage


class SearchModule:

    def __init__(self, actions):
        self.actions = actions
        self.search_page = SearchPage(self.actions)

    def waitForPageToLoad(self):
        self.search_page.waitForPageToLoad()

    def selectSailings(self, month, from_date, to_date):
        self.search_page.selectSailings(month, from_date, to_date)

    def selectCruiseLine(self, cruiseLine):
        self.search_page.selectCruiseLine(cruiseLine)

    def fillSearchData(self, month, from_date, to_date, cruiseLine):
        self.search_page.fillSearchData(month, from_date, to_date, cruiseLine)

    def clickSearch(self):
        self.search_page.clickSearch()
