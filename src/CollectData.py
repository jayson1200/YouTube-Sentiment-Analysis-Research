from urllib.parse import urlsplit
import scrapy;
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


def main():
    process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})

    process.crawl(CommentScraper)
    process.start()

class CommentScraper(scrapy.Spider):
    name = "comments"

    custom_settings = {
        'ROBOTSTXT_OBEY': False
    }
    def start_requests(self):
        startUrls = [
            "https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNWpoZxIiUEwzWlE1Q3BOdWxRbUtPUDNJekdsYWN0V1c4dklYX0hFUA%3D%3D"
        ]

        for url in startUrls:
            yield scrapy.Request(url =url, callback=self.parse)
    
    def parse(self, response):
        
        vidLinkExtractor = LxmlLinkExtractor(restrict_css = "div.dismissable") 

        vidLinks = vidLinkExtractor.extract_links(response)
        
        vidUrls = []

        for link in vidLinks:
            vidUrls.append(link.url)

        # newsVidLinks = response.css("ytd-thumbnail.style-scope.ytd-video-renderer a::href")
        
        # yield from response.follow_all(newsVidLinks, callback=self.parse)
        print(vidUrls)








if __name__ == "__main__":
    main()