import datetime
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

# Grabs comments from url of video
class Video:
    
    def __init__(self, videoURL):
        self.videoURL = videoURL
        self.usable = True

        browser = webdriver.Chrome(PATH)
        browser.get(videoURL)

        time.sleep(5)
        
        browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight/4)")

        time.sleep(5)
        
        self.comments = []

        if len(browser.find_elements_by_xpath('//*[@id="message"]/span')) <=  0:
  
            elems = browser.find_elements_by_xpath('//*[@id="content-text"]')

            self.howManyComment = 0

            if len(elems) >= 15:
                self.howManyComments = 15
            else:
                self.howManyComments = len(elems)
            
            for i in range(0, self.howManyComments):
                self.comments.append(elems[i].text)
        else :
            print("Comments are turned off on this video")
            self.usable =False

        browser.quit()
        
    
    def getComments(self):
        return self.comments
    
    def getVideoURL(self):
        return self.videoURL

    def isUsable(self):
        return self.usable
    
    # This will print when an instance of this object is put into a print function
    def __str__(self):
        return "The URL is %s and there are %i comments" % (self.videoURL, len(self.comments))
    
        