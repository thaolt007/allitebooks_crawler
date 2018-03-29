# -*- coding: utf-8 -*-
import scrapy
import sqlite3
from allitebooks.items import EbookInfoItem
from scrapy.http import Request

class EbookInfoSpider(scrapy.Spider):
	name = 'ebookinfo'
	allowed_domains = ['allitebooks.com']
	start_urls = ['http://www.allitebooks.com/']

	def __init__(self):
		conn = sqlite3.connect('allitebooks.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()
		self.ebooks = c.execute('select * from allitebooks_ebook').fetchall()
		conn.close()

	def parse(self, response):
		for ebook in self.ebooks:
			link = ebook['ebook_link']
			yield Request(link, dont_filter=True, callback=self.parse_info, meta={'ebook':ebook})

	def parse_info(self, response):
		r = response
		ebook = r.meta['ebook']
		item = EbookInfoItem()
		item['ebook_id'] = ebook['ebook_id']
		item['ebook_title'] = ebook['ebook_title']
		item['ebook_link'] = ebook['ebook_link']
		item['ebook_thumbnail'] = ebook['ebook_thumbnail']
		item['ebook_authors'] = ebook['ebook_authors']
		try:
			item['ebook_subtitle'] = r.css('h4::text').extract()[0]
		except:
			item['ebook_subtitle'] = ''
		# try: 
		data = r.css('.book-detail dl dd')
		try: item['ebook_isbn'] = data[1].css('::text').extract()[0].strip()
		except: item['ebook_isbn'] = ''

		try: item['ebook_year'] = data[2].css('::text').extract()[0].strip()
		except: item['ebook_year'] = ''

		try: item['ebook_pages'] = data[3].css('::text').extract()[0].strip()
		except: item['ebook_pages'] = ''

		try: item['ebook_language'] = data[4].css('::text').extract()[0].strip()
		except: item['ebook_language'] = ''

		try: item['ebook_filesize'] = data[5].css('::text').extract()[0].strip().split()[0]
		except: item['ebook_filesize'] = ''

		try: item['ebook_fileformat'] = data[6].css('::text').extract()[0].strip()
		except: item['ebook_fileformat'] = ''

		try: item['ebook_category'] = data[7].css('a::text').extract()[0].strip().lower()
		except: item['ebook_category'] = ''

		try: item['ebook_description'] = r.css('.entry-content').extract()[0]
		except: item['ebook_description'] = ''

		try: item['ebook_linkdownload'] = r.css('span.download-links a::attr(href)').extract()[0]
		except: item['ebook_linkdownload'] = ''

		try: item['ebook_linkreadonline'] = r.url + r.css('span.download-links a::attr(href)').extract()[1].strip('/')
		except: item['ebook_linkreadonline'] = ''

		yield item