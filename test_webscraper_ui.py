
import random
import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Web_Scraper import web_Scraper
from unittest.mock import patch

class TestWebScraper(unittest.TestCase):
    '''
    This is a class implemented to test the 
    webscraper code developed in python
    '''
    @classmethod
    def setUp(self):
        self.web_Scraper = web_Scraper()
        self.url = ""
        self.website_list = []
        self.coin_dict = {}
        self.directory = ""

    def test_close_unwanted(self):
        aValue = self.web_Scraper.close_unwanted()
        self.assertTrue(aValue)

    def test_click_next_page(self):
        self.web_Scraper.close_unwanted()
        self.web_Scraper._scan_page(3, 2)
        time.sleep(0.5)
        self.web_Scraper._get_list_of_coin_links()
        self.url = self.web_Scraper._click_next_page()
        self.assertEqual(self.url, "https://coinmarketcap.com/?page=2")


    def test_get_list_of_coin_links(self):
        self.web_Scraper.close_unwanted()
        self.web_Scraper._scan_page(3, 2)
        self.website_list = self.web_Scraper._get_list_of_coin_links()
        self.assertAlmostEqual(len(self.website_list), 100)

    def test_retrieve_Text_And_Image(self):
        self.web_Scraper.close_unwanted()
        self.web_Scraper._scan_page(3,2)
        self.web_Scraper._get_list_of_coin_links()
        coin_index = random.randrange(0, len(self.web_Scraper.list_of_coin_links)) 
        self.coin_dict = self.web_Scraper._retrieve_Text_And_Image(coin_index)
        for value in self.coin_dict.items():
            if 'none' in value:
                self.assertFalse
            else:
                self.assertTrue

    def test_saved_data(self):
        self.web_Scraper.close_unwanted()
        self.web_Scraper._scan_page(3,2)
        self.web_Scraper._get_list_of_coin_links()
        coin_index = random.randrange(0, len(self.web_Scraper.list_of_coin_links)) 
        self.coin_dict = self.web_Scraper._retrieve_Text_And_Image(coin_index)
        self.directory = self.web_Scraper._save_data()
        if(os.path.isdir('./raw_data/*/*.jpg') and os.path.isdir('./raw_data/*/*.json')):
            self.assertTrue
        else:
            self.assertFalse
        self.web_Scraper.driver.quit() 

if __name__ == "__main__":
    unittest.main(verbosity=3)