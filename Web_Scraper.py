'''
This is a python program written to
scrap neccessary data from a financial website
i.e. coinmarketcap.com.
'''
import time
import datetime
import os
import json
import random
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

class web_Scraper:
    '''
    This is a class implemented to scrap required
    Data/information from the chosen financial website.
    '''

    def __init__(self):
        ''' 
        web scrapper class constructor to initialize the object
        parameters 
        ----------
        self - an instance of the web_scraper

        type
        ----
         Object - an Object of class web_scraper

        '''
        self.count = 0 # variable for number of Cryptocurrencies data acquired
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        URL = "https://www.coinmarketcap.com"
        self.driver.get(URL)
        time.sleep(1) 
        self.list_of_coin_links = []
        self.coin_name = ""
        self.coin_price = ""
        self.coin_rank = ""
        self.coin_image_link = ""
        self.coin_dict = {}

    def accept_cookies(self) -> bool:
        '''
        this method accepts the cookies and returns True/False on the success

        Returns
        -------
        bool:
            True, if method successfully accepts the cookies else returns False. 
        ''' 
        self.driver.maximize_window()
        try:
            accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//div[@class="cmc-cookie-policy-banner__close"]')
            accept_cookies_button.click()
            return True
        except:
            print("Couldn't find button")
            return False #if accept cookies button not found

    def _click_next_page(self):
        '''
        This function finds and clicks the next page button

        Returns
        -------
        str:
            the link that the driver is currently at the end of this method.

        '''
        find_class = self.driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[7]/div[1]/div')
        find_next = find_class.find_element(by=By.XPATH, value='//li[@class="next"]')
        a_tag = find_next.find_element(by=By.TAG_NAME, value='a')
        list_of_coin_links = a_tag.get_attribute('href')      
        sleep(1)
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
        script = "window.scrollTo({left: 0, top: document.body.scrollHeight, behavior : 'smooth'});"
        for _ in range(no_of_scans):
            self.driver.execute_script(script)
            sleep(wait_time)
            self.driver.execute_script("window.scrollTo({left: 0, top: -(document.body.scrollHeight), behavior : 'smooth'});")
            sleep(wait_time)
            self.driver.execute_script(script)
        return self.driver


    def _get_list_of_coin_links(self) -> list:
        '''
        gets a list with all the list_of_coin_links in the current page
        Returns
        -------
        list_of_coin_links: list
            A list with all the links to different coin pages from the table.
        '''
        self._scan_page(3, 1)
        crypto_table = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[5]/table')
        crypto_list = crypto_table.find_elements(by=By.XPATH, value='//tbody/tr/td[3]/div')

        for crypto_currency in crypto_list:
            a_tag = crypto_currency.find_element(by=By.TAG_NAME, value='a')       
            list_of_coin_links = a_tag.get_attribute('href')
            self.list_of_coin_links.append(list_of_coin_links)

        print(" number of coin pages acquired: ", len(self.list_of_coin_links))    
        return self.list_of_coin_links
       
    def _download_coin_logo(self):
        '''
        This function can be used to download the coin logo 
        from the coinmarketcap.com website's page.
        '''
        img_data = requests.get(self.coin_dict["image list_of_coin_links"]).content
        with open(str(self.coin_dict["coin name"]) + ' logo.jpg', 'wb') as handler:
            handler.write(img_data)
        

    def _retrieve_Text_And_Image(self) -> dict:
        '''
        This function can be used to 
        retrieve the text and image from a webpage 
        containing information on a CryptoCurrency 
        randomly chosen from the first two pages.

        Return
        ----------
        coin_dict: dict
            This is a dictionary to store the data scraped on the coin.

        '''
        coin_index = random.randrange(0, len(self.list_of_coin_links)) 
        coin_link = self.list_of_coin_links[coin_index]
        print(coin_link)
        self.driver.get(coin_link)
        coin_class = self.driver.find_element(by=By.XPATH, value = '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div')
        try:
            self.coin_name = coin_class.find_element(by=By.XPATH, value = './div[1]/div[1]/h2/span').text
            coin_image = coin_class.find_element(by=By.XPATH, value = './div[1]/div[1]/img')
            self.coin_image_link = coin_image.get_attribute("src")
            self.coin_price = self.driver.find_element(by=By.XPATH, value = '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div').text
            self.coin_rank = coin_class.find_element(by=By.XPATH, value='./div[1]/div[2]/div[1]').text
        except Exception as e:
            print("Oops, couldn't find an web element!")
            pass
        ct = datetime.datetime.now()
        ts = ct.timestamp()
        self.coin_id = str(self.coin_name) + '#' + str(id(self.coin_name) )
        self.coin_dict = {"coin id":self.coin_id,"coin name":self.coin_name, "image list_of_coin_links":self.coin_image_link, "coin price": self.coin_price, "time stamp": ts, "coin rank":self.coin_rank}
        print(self.coin_dict)
        return self.coin_dict

    def _save_data(self) -> str:
        '''
        This function can be used to save the information
        acquired from finance website on a specific cryptocurrency
        locally on a json file.
        p_dir_name is parent directory name.
        c_dir_name is child directory name,
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
        self._download_coin_logo()
        jsonString = json.dumps(self.coin_dict)
        jsonFile = open("data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        os.chdir('../..')
        return create_directories

if __name__ == '__main__':
    webscraper = web_Scraper()
    webscraper.accept_cookies()
    webscraper._get_list_of_coin_links()
    if(len(webscraper.list_of_coin_links) < 90):
        webscraper._get_list_of_coin_links()
    webscraper._click_next_page()
    webscraper._get_list_of_coin_links()
    if(len(webscraper.list_of_coin_links) < 190):
        webscraper._get_list_of_coin_links()
    webscraper._retrieve_Text_And_Image()
    webscraper._save_data()
    webscraper.driver.quit() # this closes the opened browser before this program terminates
    