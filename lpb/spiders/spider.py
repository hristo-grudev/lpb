import scrapy

from scrapy.loader import ItemLoader
from ..items import LpbItem
from itemloaders.processors import TakeFirst


class LpbSpider(scrapy.Spider):
	name = 'lpb'
	start_urls = ['https://www.lpb.lv/']

	def parse(self, response):
		post_links = response.xpath('//h5/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//article[@class="news-item"]/h1//text()').get()
		description = response.xpath('//article[@class="news-item"]//p//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//article[@class="news-item"]/span//text()').get()

		item = ItemLoader(item=LpbItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
