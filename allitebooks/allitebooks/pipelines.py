# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy import create_engine, Table, Column, MetaData, Integer, Text, Float
from scrapy.exceptions import DropItem

class CatePipeline(object):

    def __init__(self):
        _engine = create_engine("sqlite:///allitebooks.db")
        _connection = _engine.connect()
        _metadata = MetaData()
        _stack_items = Table("allitebooks_category", _metadata,
                             Column("id", Integer, primary_key=True),
                             Column('cate_id', Integer, unique=True),
                             Column('cate_link', Text),
                             Column('cate_text', Text),
                             Column('cate_father', Integer),
                             Column('cate_level', Integer))
        _metadata.create_all(_engine)
        self.connection = _connection
        self.stack_items = _stack_items

    def process_item(self, item, spider):
        is_valid = True
        for data in item:
            if not data:
                is_valid = False
                raise DropItem("Missing %s!" % data)
        if is_valid:
            ins_query = self.stack_items.insert().values(
                cate_id = item['cate_id'],
				cate_link = item['cate_link'],
				cate_text = item['cate_text'],
				cate_father = item['cate_father'],
				cate_level = item['cate_level'])
            self.connection.execute(ins_query)
        return item

class EbookPipeline(object):

    def __init__(self):
        _engine = create_engine("sqlite:///allitebooks.db")
        _connection = _engine.connect()
        _metadata = MetaData()
        _stack_items = Table("allitebooks_ebookinfo", _metadata,
                             Column("id", Integer, primary_key=True),
                             Column('ebook_id', Integer, unique=True),
                             Column('ebook_title', Text),
                             Column('ebook_thumbnail', Text),
                             Column('ebook_link', Text),
                             Column('ebook_authors', Text))

        _metadata.create_all(_engine)
        self.connection = _connection
        self.stack_items = _stack_items

    def process_item(self, item, spider):
        is_valid = True
        for data in item:
            if not data:
                is_valid = False
                raise DropItem("Missing %s!" % data)
        if is_valid:
            ins_query = self.stack_items.insert().values(
                ebook_id = item['ebook_id'],
                ebook_title = item['ebook_title'],
                ebook_thumbnail = item['ebook_thumbnail'],
                ebook_link = item['ebook_link'],
                ebook_authors = item['ebook_authors'])
            self.connection.execute(ins_query)
        return item

class EbookInfoPipeline(object):

    def __init__(self):
        _engine = create_engine("sqlite:///allitebooks.db")
        _connection = _engine.connect()
        _metadata = MetaData()
        _stack_items = Table("allitebooks_ebookinfo", _metadata,
                             Column("id", Integer, primary_key=True),
                             Column('ebook_id', Integer, unique=True),
                             Column('ebook_title', Text),
                             Column('ebook_subtitle', Text),
                             Column('ebook_thumbnail', Text),
                             Column('ebook_link', Text),
                             Column('ebook_authors', Text),
        					 Column('ebook_isbn', Text),
        					 Column('ebook_year', Integer),
        					 Column('ebook_pages', Integer),
        					 Column('ebook_language', Text),
        					 Column('ebook_filesize', Text),
        					 Column('ebook_fileformat', Text),
        					 Column('ebook_category', Text),
        					 Column('ebook_description', Text),
        					 Column('ebook_linkdownload', Text))

        _metadata.create_all(_engine)
        self.connection = _connection
        self.stack_items = _stack_items

    def process_item(self, item, spider):
        is_valid = True
        for data in item:
            if not data:
                is_valid = False
                raise DropItem("Missing %s!" % data)
        if is_valid:
            ins_query = self.stack_items.insert().values(
                ebook_id = item['ebook_id'],
                ebook_title = item['ebook_title'],
                ebook_subtitle = item['ebook_subtitle'],
				ebook_thumbnail = item['ebook_thumbnail'],
				ebook_link = item['ebook_link'],
				ebook_authors = item['ebook_authors'],
				ebook_isbn = item['ebook_isbn'],
				ebook_year = item['ebook_year'],
				ebook_pages = item['ebook_pages'],
				ebook_language = item['ebook_language'],
				ebook_filesize = item['ebook_filesize'],
				ebook_fileformat = item['ebook_fileformat'],
				ebook_category = item['ebook_category'],
				ebook_description = item['ebook_description'],
				ebook_linkdownload = item['ebook_linkdownload'])
            self.connection.execute(ins_query)
        return item