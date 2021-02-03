

class Entry:

    def __init__(self, sentiment, magnitude, djia, nasdaq, nyse, dateTime):
        self.sentiment = sentiment
        self.magnitude = magnitude
        self.djia = djia
        self.nasdaq = nasdaq
        self.nyse = nyse
        self.dateTime = dateTime

    def getSentiment(self):
        return self.sentiment

    def getMagnitude(self):
        return self.magnitude

    def getDJIA(self):
        return self.djia

    def getNASDAQ(self):
        return self.nasdaq
    
    def getNYSE(self):
        return self.nyse

    def getDateTime(self):
        return self.dateTime

        