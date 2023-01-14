from odysseus_modules.pages.B2BDefaultPage import B2BDefaultPage


class B2BDefaultModule:

    def __init__(self, actions):
        self.actions = actions
        self.defaultPage = B2BDefaultPage(actions)

    def selectAffiliate(self, childSiid):
        self.defaultPage.selectAffiliate(childSiid)



