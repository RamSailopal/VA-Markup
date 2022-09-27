import scrapy
import os
import wget
class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.va.gov/vdl/section.asp?secid=2']

    def parse(self, response):
        f = open("links.txt", "a")
        try:
           for title in response.xpath('//td/a'):
              if (title.xpath('@href').extract()[0].find(".docx") != -1):
                 print(title.xpath('@href').extract()[0])
                 f.write(title.xpath('@href').extract()[0] + '\n')
        except:
           print("")
        try:
           for next_page in response.xpath('//td/a'):
              yield response.follow(next_page, self.parse)
        except:        
           print("")
        f.close()
