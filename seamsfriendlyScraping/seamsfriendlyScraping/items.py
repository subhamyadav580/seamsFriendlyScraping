import scrapy


class SeamsfriendlyscrapingItem(scrapy.Item):
    Label = scrapy.Field()
    Images = scrapy.Field()
    Description = scrapy.Field()
    Prices = scrapy.Field()

