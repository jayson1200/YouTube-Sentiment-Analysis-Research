from selenium import webdriver
from Video import Video

PATH = "C:\Program Files (x86)\chromedriver.exe"

def main():
    url = "https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNWpoZxIiUEwzWlE1Q3BOdWxRbUtPUDNJekdsYWN0V1c4dklYX0hFUA%3D%3D"
    browser = webdriver.Chrome(PATH)
    browser.get(url)

    

    
    newsVideos = []

    for pageElem in browser.find_elements_by_xpath('//*[@id="thumbnail"]'):
        newVid = Video(pageElem.get_attribute("href"))
        newsVideos.append(newVid)

        print(newVid)
    

    
    










if __name__ == "__main__":
    main()