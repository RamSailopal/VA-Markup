import scrapy
import os
import wget
class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.va.gov/vdl/application.asp?appid=5']

    def parse(self, response):
        for title in response.xpath('//td/a'):
           if (title.xpath('@href').extract()[0].find(".docx") != -1):
              print(title.xpath('@href').extract()[0])
              link='https://www.va.gov/vdl/' + title.xpath('@href').extract()[0]
              filename=wget.download(link)
              filnamnoext=filename.replace(".docx",".md")
              os.system('pandoc --extract-media=images -s ' + filename + ' -t markdown -o ' + filnamnoext)
        for next_page in response.css('a.next'):
           yield response.follow(next_page, self.parse)
        os.system("rm /home/tmp/*.docx")
