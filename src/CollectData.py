from selenium import webdriver
from Video import Video

PATH = "C:\Program Files (x86)\chromedriver.exe"

def main():
    url = "https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNWpoZxIiUEwzWlE1Q3BOdWxRbUtPUDNJekdsYWN0V1c4dklYX0hFUA%3D%3D"
    browser = webdriver.Chrome(PATH)
    browser.get(url)
    

    

    
    newsVideos = []

    webVidElems = browser.find_elements_by_xpath('//*[@id="thumbnail"]')

    for pageElem in webVidElems:
        
        hrefVal = pageElem.get_attribute("href")
        if hrefVal == None:
            continue

        newVid = Video(hrefVal)
        
        if newVid.isUsable == False:
            continue
        
        newsVideos.append(newVid)

        print(newVid)
    

    
    










if __name__ == "__main__":
    main()