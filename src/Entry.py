from datetime import date, datetime

class Entry:

    def __init__(self, sentiment, magnitude, djia, nasdaqComp, sp, dateTime):
        self.sentiment = sentiment
        self.magnitude = magnitude
        self.djia = djia
        self.nasdaqComp = nasdaqComp
        self.sp = sp
        self.dateTime = dateTime
        

    def getSentiment(self):
        return self.sentiment

    def getMagnitude(self):
        return self.magnitude

    def getDJIA(self):
        return self.djia

    def getNASDAQComp(self):
        return self.nasdaqComp
    
    def getSP(self):
        return self.sp

    def getDateTime(self):
        return self.dateTime

    def __str__(self):
        return " Sentiment: %f \n Magnitude: %f \n DJIA: %f \n NASDAQ Comp: %f \n S&P500: %f \n" % (
            self.sentiment, self.magnitude, self.djia, self.nasdaqComp, self.sp) + " DateTime: " + str(self.dateTime)

        