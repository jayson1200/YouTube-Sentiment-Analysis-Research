from datetime import date, datetime

class Entry:

    def __init__(self, sentiment, magnitude, djia, nasdaqComp, sp, spxl, spxs, dateTime, faultyLinks, commentsAnalyzed):
        self.sentiment = sentiment
        self.magnitude = magnitude
        self.djia = djia
        self.nasdaqComp = nasdaqComp
        self.sp = sp
        self.dateTime = dateTime
        self.spxl = spxl
        self.spxs = spxs
        self.faultyLinks = faultyLinks
        self.commentsAnalyzed = commentsAnalyzed
        

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

    def getBullETF(self):
        return self.spxl

    def getBearETF(self):
        return self.spxs

    def getFaultyLinks(self):
        return self.faultyLinks

    def getCommentsAnalyzed(self):
        return self.commentsAnalyzed

    def __str__(self):
        return " Sentiment: %f \n Magnitude: %f \n DJIA: %f \n NASDAQ Comp: %f \n S&P500: %f \n 3XBullShares/SPXL: %f \n 3XBearShares/SPXS: %f \n" % (
            self.sentiment, self.magnitude, self.djia, self.nasdaqComp, self.sp, self.spxl, self.spxs) + " DateTime: " + str(self.dateTime) + "\n %i links were faulty" % (self.faultyLinks) + "\n %i comments were analyzed" % (self.commentsAnalyzed)

        