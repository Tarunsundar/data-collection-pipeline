# Data Collection pipeline
DockerHub Access Token: dckr_pat_5hBhfHxNDBFMuzHEwy2jmcC-Au4

This is a python program written to automate the process of Data collection from a chosen
website, For this project, coinmarketcap, a finance based website had been chosen.
implemented a class for the data collection schema.

    Parameters & attributes
    _______________________

    count : int
    this is count of website links collected for each coin.

    driver: webdriver.chrome()
    this is the driver to automate the process of scraping data from chrome.

    list_of_coin_links: list
    this variable will be used to store the links of coin websites collected.

    coin_name: Str
    name of the coin scraped.

    coin_price: Str
    price of the coin scraped.

    coin_image_link : Str
    link to download the coin logo.

    coin_dict: dict
    a python dictionary to store the data scraped from a chosen coin.

    
    Method
    ______

    close_unwanted()
    
    this function looks for an accept cookies tab and closes it.
    the function returns true if it finds and closes an accept cookies tab.

    _click_next_page()

    this function searches for a click next page button
    and clicks it. this function returns current URL of the chromedriver 
    after clicking the next page button.

    _scan_page()

     This function scrolls through the page multiple times and wait for some given time 
    to load the page's contents, so that they can be scrapped.

    _get_list_of_coin_links()

    Returns a list with all the list_of_coin_linkss in the current page

    _download_coin_logo()

    This function can be used to download the coin logo 
    from the coinmarketcap.com website's page.

    _get_coin_index()

    This function get's the coin index randomly,
    using the python's random function.

    _retrieve_Text_And_Image()

    This function can be used to 
    retrieve the text and image from a webpage 
    containing information on a CryptoCurrency 
    randomly chosen from the first two pages.
        
    _save_data()
    This function can be used to save the information
    acquired from finance website on a specific cryptocurrency
    locally on a json file.


