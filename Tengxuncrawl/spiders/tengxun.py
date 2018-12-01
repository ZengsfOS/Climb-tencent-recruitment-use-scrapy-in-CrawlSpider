# -*- coding: utf-8 -*-
import scrapy
# 导入链接规则匹配类，用来提取符合规则的连接
from scrapy.linkextractors import LinkExtractor
# 导入spiders的派生类CrawlSpider, Rule指定特定操作
from scrapy.spiders import CrawlSpider, Rule

from Tengxuncrawl.items import TengxuncrawlItem

class TengxunSpider(CrawlSpider):
	name = 'tengxun'
	allowed_domains = ['hr.tencent.com']
	# 指定第一页的URL,后续不用拼接
	start_urls = ["https://hr.tencent.com/position.php?&start=0"]

# 方法１
#	rules = (
#		Rule(LinkExtractor(allow=r'start=\d+'), callback='parseHtml', follow=True),
#    )
#
	
	# 每页的链接规则
	pageLink = LinkExtractor(allow=r"start=\d+")
	# 公司信息链接
	companyLink = LinkExtractor(allow=r"position_detail.php?id=\d+&keywords=&tid=0&lid=0")
	rules = (
		Rule(pageLink, callback="parseHtml", follow=True),
		Rule(companyLink, callback="companyHtml", follow=True),
	)

	def parse_item(self, response):
		i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
		return i

	def parseHtml(self, response):
        # 每个职位的节点对象列表
		baseList = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
		for base in baseList:
			item = TengxuncrawlItem()
			item["zhName"] = base.xpath('./td[1]/a/text()').extract()[0]
			item["zhLink"] = base.xpath('./td[1]/a/@href').extract()[0]
			resType = base.xpath('./td[2]/text()').extract()
			if resType:
				item["zhType"] = resType[0]
			else:
				item["zhType"] = "无"
			item["zhNum"] = base.xpath('./td[3]/text()').extract()[0]
			item["zhAddress"] = base.xpath('./td[4]/text()').extract()[0]
			item["zhTime"] = base.xpath('./td[5]/text()').extract()[0]

			yield item


	def companyHtml(self, response):
		
