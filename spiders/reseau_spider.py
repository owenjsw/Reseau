import scrapy

class Reseau(scrapy.spiders.Spider):
    name = "reseau"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.zhihu.com"
    ]
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)