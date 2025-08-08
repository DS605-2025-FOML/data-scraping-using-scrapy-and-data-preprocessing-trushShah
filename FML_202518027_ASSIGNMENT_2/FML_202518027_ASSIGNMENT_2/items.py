# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Fml202518027Assignment2Item(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    Price = scrapy.Field()
    Rating = scrapy.Field()
    Availability = scrapy.Field()
    # Product_Information = scrapy.Field()
    pass
