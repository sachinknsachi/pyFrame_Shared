import re


class StringUtils:

    @staticmethod
    def extractDomainFromURL(b2CSiteURL):
        return b2CSiteURL.replace("http://", "").replace("https://", "").split("/")[0]

    @staticmethod
    def extractValueFromPattern(pattern, value, group=1):
        # search for the pattern in the string
        match = re.search(pattern, value)
        # extract the value using the group() method
        return match.group(group)





