from time import sleep
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options;
from selenium.common.exceptions import NoSuchElementException        
import os
from ..items import SeamsfriendlyscrapingItem


class ShortSpider(scrapy.Spider):
    name = 'seamsFriendlySpider'


    def start_requests(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(f'{os.getcwd()}/chromedriver', options=self.options)
        self.driver.get('https://in.seamsfriendly.com/collections/shorts')
        sleep(3)
        flag = True
        self.count = 0
        if self.count == 0:
            self.count += 1
            yield scrapy.Request(self.driver.current_url)

        while flag:
            if self.check_exists_by_xpath('//*[@id="shopify-section-collection-template"]/section/div[3]/div[2]/div[2]/div[4]/div/div[3]/div[2]/button') and self.count > 0:
                self.driver.find_element_by_xpath('//*[@id="shopify-section-collection-template"]/section/div[3]/div[2]/div[2]/div[4]/div/div[3]/div[2]/button').click()
                sleep(2)
                yield scrapy.Request(self.driver.current_url)
                flag = True
            else:
                flag = False

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
        
    def parse(self, response, **kwargs):
        items = SeamsfriendlyscrapingItem()
        blocks = response.xpath('/html/body/div[6]/main/div[1]/section/div[3]/div[2]/div[2]/div[2]/div/div')
        for block in blocks:
            label = block.css('div div div.label_icon::text').extract()
            img = block.css('img').xpath('@src').extract()
            desc = block.css('h2 a::text').extract()
            images = [f"https:{im}" for im in img]
            prices = block.css('div div div div span.ProductItem__Price::text').extract()
            items['Label'] = label
            items['Images'] = images
            items['Description'] = desc
            items['Prices'] = prices
            yield items

