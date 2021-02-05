import time
import csv
import os

from selenium import webdriver
from Video import Video
from google.cloud import language_v1
from Entry import Entry
from datetime import datetime
from selenium.common.exceptions import StaleElementReferenceException



PATH = "C:\Program Files (x86)\chromedriver.exe"


def main():
    while(True):

        hour = datetime.now().hour
        if hour >= 4 and hour <= 20:

            minute = datetime.now().minute

            if minute == 30 or minute == 0:
                newEntry = fillNewEntry(test = False)

                newValues = [newEntry.getSentiment(), newEntry.getMagnitude(), 
                newEntry.getDJIA(),newEntry.getNASDAQComp(),
                newEntry.getSP(), newEntry.getBullETF(), 
                newEntry.getBearETF(), newEntry.getDateTime(), 
                newEntry.getFaultyLinks(), newEntry.getCommentsAnalyzed()]

                with open('YoutubeData.csv', 'a', newline='') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(newValues)

                time.sleep(60)


def fillNewEntry(**kwargs):
    youtubeURL = "https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNWpoZxIiUEwzWlE1Q3BOdWxRbUtPUDNJekdsYWN0V1c4dklYX0hFUA%3D%3D"
    sp500URL = "https://www.google.com/finance/quote/.INX:INDEXSP"
    djiaURL = "https://www.google.com/finance/quote/.DJI:INDEXDJX"
    ndaqCompURL = "https://www.google.com/finance/quote/.IXIC:INDEXNASDAQ"
    bullSPXLURL = "https://www.google.com/finance/quote/SPXL:NYSEARCA?sa=X&ved=2ahUKEwin2vP45dDuAhVPhuAKHZkHAB0Q3ecFMAB6BAgMEBk"
    bearSPXSURL = "https://www.google.com/finance/quote/SPXS:NYSEARCA?sa=X&ved=2ahUKEwiQ07GW5tDuAhXJX98KHdDyBowQ3ecFMAB6BAgGEBk"

    browser = webdriver.Chrome(PATH, service_log_path=os.devnull)
    
    browser.get(sp500URL)
    sp500Price = browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/main/div[2]/c-wiz/div/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/span/div/div').text
    
    browser.get(djiaURL)
    djiaPrice = browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/main/div[2]/c-wiz/div/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/span/div/div').text
    
    browser.get(ndaqCompURL)
    ndaqCompPrice = browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/main/div[2]/c-wiz/div/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/span/div/div').text
    
    browser.get(bullSPXLURL)

    spxlBullPrice = browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/main/div[2]/c-wiz/div/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/span/div/div').text

    browser.get(bearSPXSURL)

    spxsBearPrice = browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/main/div[2]/c-wiz/div/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/span/div/div').text

    browser.get(youtubeURL)
    

    client = language_v1.LanguageServiceClient.from_service_account_json("C:\\Users\\jayso\Documents\\YoutubeSentimentKey.json")

    docType = language_v1.Document.Type.PLAIN_TEXT

    docLang = "en"

    newsVideos = []

    webVidElems = browser.find_elements_by_xpath('//*[@id="thumbnail"]')

    currentTime = datetime.now()

    howManyUnparsable = 0

    # For quick test purposes
    if kwargs.get("test") == True:
        webVidElems = [webVidElems[1]]

    for pageElem in webVidElems:
        #Stale element
        try:
            hrefVal = pageElem.get_attribute("href")
        except StaleElementReferenceException as e:
            print("Could not get element")
            print("Moving on")
            howManyUnparsable += 1
            continue


        if hrefVal == None:
            continue

        newVid = Video(hrefVal)
        
        if newVid.isUsable == False:
            continue
        
        newsVideos.append(newVid)

    allVidCommentText = ""
    howManyComments = 0

    for i in range(0, len(newsVideos)):
        for j in range(0, len(newsVideos[i].getComments())):
            allVidCommentText += " %s" % newsVideos[i].getComments()[j]
            howManyComments+=1
    
    commentDocument = {
        "content" : allVidCommentText,
        "type_" : docType,
        "language" : docLang,
    }

    sentimentResponse = client.analyze_sentiment(request = {
        "document" : commentDocument,
        "encoding_type" : language_v1.EncodingType.UTF8
    })

    overallYouTubeSentiment = sentimentResponse.document_sentiment.score
    overallYouTubeMagnitude = sentimentResponse.document_sentiment.magnitude

    browser.close()
    
    newEntry = Entry(overallYouTubeSentiment, overallYouTubeMagnitude, 
    float(djiaPrice.replace(',','')), float(ndaqCompPrice.replace(',','')), float(sp500Price.replace(',','')), float(spxlBullPrice.replace(',','').replace('$','')), float(spxsBearPrice.replace(',','').replace('$','')), 
    currentTime, howManyUnparsable, howManyComments)
    
    print(newEntry)

    return newEntry 
    
    

if __name__ == "__main__":
    main()