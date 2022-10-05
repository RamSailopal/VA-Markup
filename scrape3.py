import scrapy
import os
import wget
class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.va.gov/vdl/application.asp?appid=6']
    def parse(self, response):
        try:
           link='https://www.va.gov/vdl/'
           for title in response.xpath('//tr'):
              sect=response.xpath('//*[@id="tier4innerContent"]/p').css('::text').get().replace("Section","")
              pack=response.xpath('//*[@id="tier4innerContent"]/h2[2]').css('::text').get()
              cnt=0
              doc="<td></td>"
              pdf="<td></td>"
              for title1 in title.xpath('td'):
              #print(title.xpath('td').css('::text').get())
                 if cnt==0:
                    titl=title1.css('::text').get()
                 if cnt==3:
                    for title2 in title1.css('::text'):
                       if title2.get()=="PDF":
                          pdf='<td><a href="' + link + title1.xpath('a').xpath('@href').extract()[0] + '">Link</a></td>'
                       elif title2.get()=="DOCX":
                          doc='<td><a href="' + link + title1.xpath('a').xpath('@href').extract()[1] + '">Link</a></td>'
                    print('<tr><td>' + sect + '</td><td>' + pack + '</td><td>' + titl + '</td>' + doc + pdf + '</tr>\n')
                 cnt=cnt+1
        except:
           print("")
        try:
           for next_page in response.xpath('//td/a'):
              yield response.follow(next_page, self.parse)
        except:
            print("")

