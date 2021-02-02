import datetime
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

# Grabs comments from url of video
class Video:
    
    def __init__(self, videoURL):
        self.videoURL = videoURL

        browser = webdriver.Chrome(PATH)
        browser.get(videoURL)
        # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        
        self.comments = []

        
        time.sleep(5)
        
        elems = browser.find_elements_by_xpath('//*[@id="content-text"]')
        
        for i in range(0, 15):
            self.comments.append(elems[i].text)
        
    
    def getComments(self):
        return self.comments
    
    def getVideoURL(self):
        return self.videoURL
    
    # This will print when an instance of this object is put into a print function
    def __str__(self):
        return "The URL is %s and there are %i comments" % (self.videoURL, len(self.comments))
    
        