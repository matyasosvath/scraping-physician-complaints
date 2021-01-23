import scrapy

class PhysicianSpiderSpider(scrapy.Spider):
    name = 'physician_spider'
    allowed_domains = ['physician']
    start_urls = ['physician']

    def parse(self, response):

        archive =  response.xpath('//ul[@class="archive-list"]/li/a/@href').extract() 
        for het in archive:
        	yield scrapy.Request(url=het, callback=self.parse_hetek)

    def parse_hetek(self, response):
    	heti_blog_linkek =  response.xpath('//a[@class="post-meta"]/@href').extract()
    	for heti_blog_link in heti_blog_linkek:
    		yield scrapy.Request(heti_blog_link, callback=self.parse_blog)
    
    def parse_blog(self, response):
        blog_cim = response.xpath('//h2/a/text()').extract_first()
        datum = response.xpath('//div[@id="postinfo"]/div[@id="date"]/text()').extract()
        szoveg = response.xpath('//div[@class="posts"]/p').extract()
        tags = response.xpath('//div[@class="hidden"]/a/text()').extract()
        comments = response.xpath('//div[@class="commentText"]/text()').extract()

        yield {"Title": blog_cim, "Datum": datum, "Content": szoveg, "URL": response.url, "Tags": tags, "Comments": comments}
