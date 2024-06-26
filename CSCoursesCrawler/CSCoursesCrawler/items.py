# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CscoursescrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    prerequisites=scrapy.Field()
    lecture = scrapy.Field()
    lab = scrapy.Field()
    credits = scrapy.Field()
    pass
