
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
    def setUp(self):
        self.web_Scraper = web_Scraper()
        self.aValue = self.web_Scraper.accept_cookies()
        self.url = ""
        self.website_list = []
        self.coin_dict = {}
        self.directory = ""

    def test_accept_cookies(self):
        self.assertTrue(self.aValue)

    def test_click_next_page(self):
        time.sleep(0.5)
        self.web_Scraper._get_list_of_coin_links()
        self.url = self.web_Scraper._click_next_page()
        self.assertEqual(self.url, "https://coinmarketcap.com/?page=2")


    def test_get_list_of_coin_links(self):
        self.website_list = self.web_Scraper._get_list_of_coin_links()
        self.assertAlmostEqual(len(self.website_list), 100)

    def test_retrieve_Text_And_Image(self):
        self.web_Scraper._get_list_of_coin_links()
        self.coin_dict = self.web_Scraper._retrieve_Text_And_Image()
        for dict_item in self.coin_dict.items(): 
            if None in dict_item:
                self.assertFalse
            else:
                self.assertTrue

    def test_saved_data(self):
        self.web_Scraper._get_list_of_coin_links()
        self.coin_dict = self.web_Scraper._retrieve_Text_And_Image()
        self.directory = self.web_Scraper._save_data()
        if(os.path.isdir('./raw_data/*/*.jpg') and os.path.isdir('./raw_data/*/*.json')):
            self.assertTrue
        else:
            self.assertFalse

    def tearDown(self):
        self.web_Scraper.driver.quit() 

if __name__ == "__main__":
    unittest.main(verbosity=3)