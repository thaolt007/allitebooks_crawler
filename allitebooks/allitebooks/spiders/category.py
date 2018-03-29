# -*- coding: utf-8 -*-
import scrapy
from allitebooks.items import CateItem

class CateSpider(scrapy.Spider):
	name = 'cate'
	allowed_domains = ['allitebooks.com']
	start_urls = ['http://allitebooks.com/']

	def parse(self, response):
		r = response
		menu_items = r.css('#menu-allitebooks-com > li > ul > li')
		for menu_item in menu_items:
			mi_id = menu_item.css('::attr(id)').extract()[0].split('-')[-1]
			mi_link = menu_item.css('a::attr(href)').extract()[0].split('/')[-2]
			mi_text = menu_item.css('a::text').extract()[0]
			mi_father = 0
			mi_level = 1
			submenus = menu_item.css('ul > li')
			
			cate_item = CateItem()
			cate_item['cate_id'] = mi_id
			cate_item['cate_link'] = mi_link
			cate_item['cate_text'] = mi_text
			cate_item['cate_father'] = mi_father
			cate_item['cate_level'] = mi_level
			yield cate_item

			for submenu in submenus:
				sm_id = submenu.css('::attr(id)').extract()[0].split('-')[-1]
				sm_link = submenu.css('a::attr(href)').extract()[0].split('/')[-2]
				sm_text = submenu.css('a::text').extract()[0]
				sm_father = mi_id
				sm_level = 2

				cate_item = CateItem()
				cate_item['cate_id'] = sm_id
				cate_item['cate_link'] = sm_link
				cate_item['cate_text'] = sm_text
				cate_item['cate_father'] = sm_father
				cate_item['cate_level'] = sm_level
				yield cate_item




