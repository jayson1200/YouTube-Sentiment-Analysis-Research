from selenium import webdriver
from Video import Video
from google.cloud import language_v1

import os 

PATH = "C:\Program Files (x86)\chromedriver.exe"

def main():
    url = "https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNWpoZxIiUEwzWlE1Q3BOdWxRbUtPUDNJekdsYWN0V1c4dklYX0hFUA%3D%3D"
    browser = webdriver.Chrome(PATH)
    browser.get(url)

    client = language_v1.LanguageServiceClient.from_service_account_json("C:\\Users\\jayso\Documents\\YoutubeSentimentKey.json")

    docType = language_v1.Document.Type.PLAIN_TEXT

    docLang = "en"

    newsVideos = []

    webVidElems = browser.find_elements_by_xpath('//*[@id="thumbnail"]')

    # For quick test purposes
    # webVidElems = [webVidElems[0]]

    for pageElem in webVidElems:
        
        hrefVal = pageElem.get_attribute("href")
        if hrefVal == None:
            continue

        newVid = Video(hrefVal)
        
        if newVid.isUsable == False:
            continue
        
        newsVideos.append(newVid)

    allVidCommentText = ""

    for i in range(0, len(newsVideos)):
        for j in range(0, len(newsVideos[i].getComments())):
            allVidCommentText += " %s" % newsVideos[i].getComments()[j]

    print(allVidCommentText)
    
    commentDocument = {
        "content" : allVidCommentText,
        "type_" : docType,
        "language" : docLang,
    }

    sentimentResponse = client.analyze_sentiment(request = {
        "document" : commentDocument,
        "encoding_type" : language_v1.EncodingType.UTF8
    })

    print(sentimentResponse.document_sentiment.score)
    print(sentimentResponse.document_sentiment.magnitude)


    
    










if __name__ == "__main__":
    main()