from time import sleep
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options;
from selenium.common.exceptions import NoSuchElementException        
import os

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
        title = response.css('title::text').extract_first()
        des = response.css('#shopify-section-collection-template a::text').extract()
        prices = response.css('#shopify-section-collection-template .Text--subdued::text').extract()
        yield {
            'URL' : response,
            'title_text' : title,
            'description' : des,
            'Prices' : prices
        }
