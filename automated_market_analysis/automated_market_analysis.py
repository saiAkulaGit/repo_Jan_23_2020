#!/usr/bin/env python3
# coding: utf-8


"""
    tradeMarket_analysis main objective is to scrape current market values,
    logging credentials, monitoring watch-list,
    processing data and saving in CVS file,
    using selenium this entire process is Automated,
    this data is futher used for Market predection

    VERSION : 1.0
    LICENSE : GNU GPLv3
    STYLE   : PEP 8
    AUTHOR  : AKULA.S.S.S.R.Krishna
    Date    : 12/2/2021

    PURPOSE : To automate web-scrape on going market data
    INPUT   : python3 automated_market_analysis.py
    OUTPUT  : A CSV file with current date as name is created
"""

import time
import sys
import pandas as pd
from datetime import datetime
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class tradeMarket_analysis(object):   # using selenium for browser automation
    PAGE_LOAD_TIME = 5

    def __init__(self, ):     # Opening trade site via chrome
        URL = "https://trade.angelbroking.com/"
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.set_window_size(1400, 1300)
        self.driver.get(URL)
        self.stockPrice = {}

    def login_with_credentials(self, user_name, password):
        element = self.driver.find_element_by_id("txtUserID")
        element.send_keys(user_name)
        element = self.driver.find_element_by_id("txtTradingPassword")
        element.send_keys(password)
        element.send_keys(Keys.RETURN)
        # logging credentials and waiting for page to load
        time.sleep(self.PAGE_LOAD_TIME)
        element = self.driver.find_element_by_id("mnMarkets")
        element.click()
        # switched to markets & waiting for page to load
        time.sleep(self.PAGE_LOAD_TIME)

    def date_time_now(self, ):
        now = str(datetime.now()).split()
        return now[0], now[1][0:5]

    def write_into_file(self, ):
        # converting dictionary into dataframe
        data = pd.DataFrame.from_dict(self.stockPrice)
        day_, time_ = self.date_time_now()
        # saving data  in a CSV file
        data.to_csv(day_ + '.csv')
        print(' Created file ', day_ + '.csv')

    def process_data(self, data):   # pre-processing the data into dictionary
        List = [x for x in data.split('\n')]
        if(len(self.stockPrice) == 0):
            for i in range(0, len(List), 5):
                sub = List[i:i+5]
                self.stockPrice[sub[0].split()[0]] = [float(sub[4])]
        else:
            for i in range(0, len(List), 5):
                sub = List[i:i+5]
                self.stockPrice[sub[0].split()[0]].append(float(sub[4]))

        # print(datetime.now().time())  # to check frequency of scrapped

    def monitor(self, ):        # starts monitoring watch-list 1
        element = self.driver.find_element_by_id("tbodyWTCHLIST1")
        data = element.text     # fetching watch-list text data
        self.process_data(data)


obj = tradeMarket_analysis()
obj.login_with_credentials("user name/Id", "password")  # entering credentials
while(True):
    try:
        obj.monitor()
    except KeyboardInterrupt:   # on keyboard interrupt Ctrl+c
        obj.write_into_file()   # writting into file
        sys.exit()
