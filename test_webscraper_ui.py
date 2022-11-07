
import random
import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Web_Scraper import web_Scraper
print("anything")
class TestWebScraper(unittest.TestCase):
    '''
    This is a class implemented to test the 
    webscraper code developed in python
    '''
    def setUp(self):
        self.web_Scraper = web_Scraper()
        self.url = ""
        self.website_list = []
        self.coin_dict = {}
        self.directory = ""

    def test_load_and_close_unwanted(self):
        web_Scraper.load_and_close_unwanted(web_Scraper)
        web_Scraper.assertIn("coinmarketcap", web_Scraper.driver.title)
        try:
            accept_cookies_button = web_Scraper.driver.find_element(by= By.XPATH, value='//div[@class="cmc-cookie-policy-banner__close"]')
            self.assertFalse
        except:
            self.assertTrue

    def test_click_next_page(self):
        web_Scraper._scan_page()
        time.sleep(0.5)
        self.url = web_Scraper._click_next_page()
        self.assertEqual(self.url, "https://coinmarketcap.com/?page=2")

    def test_get_list_of_coin_links(self):
        self.website_list =web_Scraper._get_list_of_coin_links()
        self.assertAlmostEqual(len(self.website_list), 100)

    def test_retrieve_Text_And_Image(self):
        coin_index = random.randrange(0, 199) 
        self.coin_dict = self.web_Scraper._retrieve_Text_And_Image(coin_index)
        for key, value in self.coin_dict.items():
            for item in value:
                if 'none' in item:
                    self.assertFalse
                else:
                    self.assertTrue

    def test_saved_data(self):
        coin_index = random.randrange(0, 199) 
        self.directory = self.web_Scraper._save_data()
        if(os.path.isdir('./raw_data/*/*.jpg') and os.path.isdir('./raw_data/*/*.json')):
            self.assertTrue
        else:
            self.assertFalse

if __name__ == "__main__":
    unittest.main()