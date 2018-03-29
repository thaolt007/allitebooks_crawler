# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class CateItem(Item):
    # define the fields for your item here like:
    # name = Field()
    cate_id = Field()
    cate_link = Field()
    cate_text = Field()
    cate_father = Field()
    cate_level = Field()

class EbookItem(Item):

	ebook_id = Field()
	ebook_thumbnail = Field()
	ebook_link = Field()
	ebook_title = Field()
	ebook_authors = Field()


class EbookInfoItem(Item):

	ebook_id = Field()
	ebook_thumbnail = Field()
	ebook_link = Field()
	ebook_title = Field()
	ebook_subtitle = Field()
	ebook_authors = Field()
	ebook_isbn = Field()
	ebook_year = Field()
	ebook_pages = Field()
	ebook_language = Field()
	ebook_filesize = Field()
	ebook_fileformat = Field()
	ebook_category = Field()
	ebook_description = Field()
	ebook_linkdownload = Field()
	ebook_linkreadonline = Field()