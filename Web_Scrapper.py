from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep

class web_Scrapper:

    def __init__(self) -> None:
        self.count = 0 # variable for number of Cryptocurrencies data acquired
        self.driver = webdriver.Chrome()
        self.link_list = []
        self.big_list = []

    def load_and_close_unwanted(self) -> webdriver.Chrome:
        '''
        Open coinmarketcap and accept the cookies

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
            #click_maybe_later_button = driver.find_element(by=By.XPATH, value='//div[@class="Maybe later"]')
            #click_maybe_later_button.click()
            time.sleep(1)

        except AttributeError: # If you have the latest version of Selenium, the code above won't run because the "switch_to_frame" is deprecated
            accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//div[@class="cmc-cookie-policy-banner__close"]')
            accept_cookies_button.click()
            #click_maybe_later_button = driver.find_element(by=By.XPATH, value='//div[@class="Maybe later"]')
            #click_maybe_later_button.click()
            time.sleep(1)

        except:
            print("Couldn't find button")
            pass #if accept cookies button not found
        return self.driver 

    def click_next_page(self):
        self.driver.execute_script("window.scrollBy(0,5500)","")
        find_class = self.driver.find_element(by=By.XPATH, value='//div[@class="sc-1t7mu4i-0 kbMknJ"]')
        find_next = find_class.find_element(by=By.XPATH, value='//li[@class="next"]')
        a_tag = find_next.find_element(by=By.TAG_NAME, value='a')
        link = a_tag.get_attribute('href')
        print(link)
        self.driver.get(link)
        #self.driver.get(link)

    def get_links(self) -> list:
        '''
        Returns a list with all the links in the current page
        Parameters
        ----------
        driver: webdriver.Chrome
            The driver that contains information about the current page
        
        Returns
        -------
        link_list: list
            A list with all the links in the page
        '''
        crypto = self.driver.find_element(by=By.XPATH, value='//table[@class="h7vnx2-2 cgeQEz cmc-table  "]')
        crypto_list = crypto.find_elements(by=By.XPATH, value='.//div[@class="sc-1prm8qw-0 PzkeQ"]')
        time.sleep(0.1)
        temp_list = crypto.find_elements(by=By.XPATH, value='.//div[@class="sc-1prm8qw-0 PzkeQ"]')
        crypto_list = temp_list + crypto_list
        self.driver.execute_script("window.scrollBy(0,1000)","")
        
        for crypto_currency in crypto_list:
            time.sleep(0.1)
            a_tag = crypto_currency.find_element(by=By.TAG_NAME, value='a')
            #temp_list = crypto.find_elements(by=By.XPATH, value='.//div[@class="sc-1prm8qw-0 PzkeQ"]')
            #crypto_list = temp_list + crypto_list
            #if(self.link_list.count == crypto_list.count):#(or link list == 100)
                #self.driver.execute_script("window.scrollBy(0,100)","")
                #crypto_list = self.driver.find_elements(by=By.XPATH, value='//table[@class="h7vnx2-2 cgeQEz cmc-table  "]')
            if(len(self.link_list) == 100):
                self.click_next(crypto)         
            link = a_tag.get_attribute('href')
            print(len(self.link_list))
            self.link_list.append(link)
            self.driver.execute_script("window.scrollBy(0,50)","")
            time.sleep(0.1)
            
        print(f'There are {len(self.link_list)} crypto currencies in this page')
        print(self.link_list)
        return self.link_list

    def retrieve_Text_And_Image(self):
        #need to implement this later
        pass

if __name__ == '__main__':
    webscrapper = web_Scrapper()
    driver = webscrapper.load_and_close_unwanted()
    webscrapper.get_links()
    webscrapper.click_next_page()
    if(webscrapper.link_list.count == 100):
        webscrapper.get_links()
    webscrapper.get_links()
    driver.quit() # this closes the opened browser before this program terminates
    