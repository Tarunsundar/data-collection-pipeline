'''
This is a python program written to
scrap neccessary data from a financial website
i.e. coinmarketcap.com.
'''

import datetime
import os
import json
import random
import shutil
from unicodedata import name
from venv import create
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from time import sleep

class web_Scraper:
    '''
    This is a class implemented to scrap required
    Data/information from the chosen financial website.
    '''

    def __init__(self) -> None:
        ''' 
        web scrapper class constructor to initialize the object
        parameters 
        ----------
        self - an instance of the web_scraper

        type
        ----
         Object - an Object

        '''
        self.count = 0 # variable for number of Cryptocurrencies data acquired
        self.driver = webdriver.Chrome()
        self.list_of_coin_links = []
        self.big_list = []
        self.coin_dict = {}

    def load_and_close_unwanted(self) -> webdriver.Chrome:
        '''
        Loads coinmarketcap webpage and accepts the cookies

        Returns
        -------
        driver: webdriver.Chrome
            This driver is already in the coinmarketcap webpage
        ''' 
        URL = "https://www.coinmarketcap.com"
        self.driver.get(URL)
        time.sleep(1) 
        #self.driver.maximize_window()
        try:
            accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//div[@class="cmc-cookie-policy-banner__close"]')
            accept_cookies_button.click()
            time.sleep(1)

        except AttributeError: # If you have the latest version of Selenium, the code above won't run because the "switch_to_frame" is deprecated
            accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//div[@class="cmc-cookie-policy-banner__close"]')
            accept_cookies_button.click()
            time.sleep(1)

        except:
            print("Couldn't find button")
            pass #if accept cookies button  found
        return self.driver 

    def _click_next_page(self):
        '''
        This function finds and clicks the next page button
        parameters 
        ----------

        self - an instance of the web_scraper

        type 
        ----

        Object - an object instance of the web_scraper class

        '''
        #self.driver.execute_script("window.scrollBy(0,5500)","")
        find_class = self.driver.find_element(by=By.XPATH, value='//div[@class="sc-1t7mu4i-0 kbMknJ"]')
        find_next = find_class.find_element(by=By.XPATH, value='//li[@class="next"]')
        a_tag = find_next.find_element(by=By.TAG_NAME, value='a')
        list_of_coin_links = a_tag.get_attribute('href')
        print(list_of_coin_links)        
        sleep(2)
        self.driver.get(list_of_coin_links)
        get_url = self.driver.current_url
        return get_url

    def _scan_page(self, no_of_scans: int, wait_time: int):
        '''
        This function scrolls through the page multiple times and wait for some given time 
        to load the page's contents, so that they can be scrapped.
        
        parameters
        ----------

        no_of_scans: int
        Number of times the webdriver needs to scroll up and down the page

        wait_time: int
        Number in time(seconds), that the program needs to stay idle before 
        executing the next command. 
        '''
        for _ in range(no_of_scans):
            self.driver.execute_script("window.scrollTo({left: 0, top: document.body.scrollHeight, behavior : 'smooth'});")
            sleep(wait_time)
            self.driver.execute_script("window.scrollTo({left: 0, top: -(document.body.scrollHeight), behavior : 'smooth'});")
            sleep(wait_time)
            self.driver.execute_script("window.scrollTo({left: 0, top: document.body.scrollHeight, behavior : 'smooth'});")
        return self.driver


    def _get_list_of_coin_links(self) -> list:
        '''
        Returns a list with all the list_of_coin_linkss in the current page
        Parameters
        ----------
        driver: webdriver.Chrome
            The driver that contains information about the current page
        
        Returns
        -------
        list_of_coin_links:>coin_index list
            A list with all the list_of_coin_linkss in the page
        '''
        crypto_table = self.driver.find_element(by=By.XPATH, value='//table[@class="h7vnx2-2 cgeQEz cmc-table  "]')
        crypto_list = crypto_table.find_elements(by=By.XPATH, value='.//div[@class="sc-1prm8qw-0 PzkeQ"]')
        time.sleep(0.1)
        
        for crypto_currency in crypto_list:
            a_tag = crypto_currency.find_element(by=By.TAG_NAME, value='a')       
            list_of_coin_links = a_tag.get_attribute('href')
            self.list_of_coin_links.append(list_of_coin_links)

        print(" number of coin pages acquired: 2", len(self.list_of_coin_links))    
        #print(f'There are {len(self.list_of_coin_links)>coin_index} crypto currencies in this page')
        #print(self.list_of_coin_links)>coin_index
        return self.list_of_coin_links
       
    def _download_coin_logo(self, fp):
        '''
        This function can be used to download the coin logo 
        from the coinmarketcap.com website's page.
        
        Parameters
        ----------
        fp: String
            The file path from where we can find
            the link to download the logo.
        '''
        img_data = requests.get(self.coin_dict["image list_of_coin_links"]).content
        with open(str(self.coin_dict["coin name"]) + ' logo.jpg', 'wb') as handler:
            handler.write(img_data)
        
    def _get_coin_index(self):
        coin_index = int(input("which coin from the first 2 pages, you would like(enter rank)\n")) 
        if(len(self.list_of_coin_links)<coin_index):            
             coin_index = random.randrange(0, 199) 
             print('invalid input, coin index not found in the first 2 pages, using random coin index: ', coin_index) 
        return coin_index

    def _retrieve_Text_And_Image(self, coin_index):
        '''
        This function can be used to 
        retrieve the text and image from a webpage 
        containing information on a CryptoCurrency 
        randomly chosen from the first two pages.
        '''
        coin_link = self.list_of_coin_links[coin_index]
        print(coin_link)
        self.driver.get(coin_link)
        coin_class = self.driver.find_element(by=By.XPATH, value = '//div[1][@class="sc-1prm8qw-0 cyZVgY top-summary-container"]')
        try:
            coin_name = coin_class.find_element(by=By.XPATH, value = '//span[@class="sc-169cagi-0 kQxZxB"]')
        except:
            coin_name = coin_class.find_element(by=By.XPATH, value = '//span[@class="sc-169cagi-0 kQxZxB tooltip"]')
        coin_name = coin_name.get_attribute('data-text')
        coin_image = coin_class.find_element(by=By.XPATH, value = '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/img')
        image_list_of_coin_links = coin_image.get_attribute("src")
        coin_price = coin_class.find_element(by=By.XPATH, value = '//div[@class="priceValue "]').text
        coin_rank = coin_class.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]').text
        # ct stores current time
        ct = datetime.datetime.now()
        # ts store timestamp of current time
        ts = ct.timestamp()
        coin_id = coin_name + '#' + str(id(coin_name) )
        self.coin_dict = {"coin id":coin_id,"coin name":coin_name, "image list_of_coin_links":image_list_of_coin_links, "coin price": coin_price, "time stamp": ts, "coin rank":coin_rank}
        print(self.coin_dict)
        return self.coin_dict

    def _save_data(self):
        '''
        This function can be used to save the information
        acquired from finance website on a specific cryptocurrency
        locally on a json file.
        '''
        # Create directory
        p_dir_name = 'raw_data'
        c_dir_name = str(self.coin_dict["coin id"])
        create_directories = p_dir_name + '/' + c_dir_name
        try:
            # Create target Directory
            os.mkdir(create_directories)
            print("Directory " , create_directories ,  " Created ") 
        except FileExistsError:
            print("Directory " , create_directories ,  " already exists")
        os.chdir(create_directories)
        self._download_coin_logo(create_directories)
        jsonString = json.dumps(self.coin_dict)
        jsonFile = open("data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        os.chdir('../..')
        return create_directories

if __name__ == '__main__':
    webscraper = web_Scraper()
    webscraper.load_and_close_unwanted()
    webscraper._scan_page(3, 2)
    webscraper._get_list_of_coin_links()
    if(len(webscraper.list_of_coin_links) < 90):
        webscraper._scan_page(3,2)
        webscraper._get_list_of_coin_links()
    webscraper._click_next_page()
    webscraper._scan_page(3, 2)
    webscraper._get_list_of_coin_links()
    coin_index = webscraper._get_coin_index()
    webscraper._retrieve_Text_And_Image(coin_index)
    webscraper._save_data()
    webscraper.driver.quit() # this closes the opened browser before this program terminates
    