# -*- coding: utf-8 -*-
import scrapy
import sqlite3
from allitebooks.items import EbookItem
from scrapy.http import Request

class EbookSpider(scrapy.Spider):
	name = 'ebook'
	allowed_domains = ['allitebooks.com']
	start_urls = ['http://www.allitebooks.com/']

	# def __init__(self):
	# 	conn = sqlite3.connect('allitebooks.db')
	# 	conn.row_factory = sqlite3.Row
	# 	c = conn.cursor()
	# 	self.cates = c.execute('select * from allitebooks_category').fetchall()
	# 	conn.close()

	def parse(self, response):
		r = response
		page_total = int( r.css('.pagination a::text').extract()[-1] )
		print(page_total)
		for page in range(page_total):
			link = r.url + 'page/' + str(page+1)
			print(link)
			yield Request(link, dont_filter=True, callback=self.parse_ebook)

	def parse_ebook(self, response):
		r = response
		articles = r.css('article')
		for article in articles:

			item = EbookItem()
			item['ebook_id'] = article.css('::attr(id)').extract()[0].split('-')[-1]
			item['ebook_title'] = article.css('h2.entry-title a::text').extract()[0]
			item['ebook_link'] = article.css('h2 a::attr(href)').extract()[0]
			item['ebook_thumbnail'] = article.css('div.entry-thumbnail a img::attr(src)').extract()[0]
			item['ebook_authors'] = ','.join( article.css('h5.entry-author a::text').extract() )

			yield item