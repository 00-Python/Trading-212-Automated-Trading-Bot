''' The Small Short Trading 212 scraper. '''
import requests
import json
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
# import sleep module from time library
from time import sleep
import os


class Trading212():
    
    def __init__(self) -> None:
        # get current working directory
        self.cwd = os.getcwd()
        # get login email from first line of file and password from second line of file credentials.txt
        with open(self.cwd+'\\credentials.txt', 'r') as f:
            self.email = f.readline().strip()
            self.password = f.readline().strip()
        self.BASE_URL = 'https://live.trading212.com/'
        
        # use firefox driver
        # self.driver = selenium.webdriver.Firefox()
        
        self.driver = uc.Chrome()
        self.driver.get(self.BASE_URL)
        # wait for page to load
        sleep(5)

    def login(self, practice=False):
        self.practice = practice
        
        # Remove the cookies popup if present
        if self.driver.find_element(By.CSS_SELECTOR, "div.Button_accent__oV2pE:nth-child(1)").is_displayed():
            self.driver.find_element(By.CSS_SELECTOR, "div.Button_accent__oV2pE:nth-child(1)").click()
        
        # enter email
        self.driver.find_element(By.CSS_SELECTOR, "div.labeled-input:nth-child(3) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)").send_keys(self.email)

        # enter password
        self.driver.find_element(By.CSS_SELECTOR, "div.labeled-input:nth-child(4) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)").send_keys(self.password)

        # click login button
        self.driver.find_element(By.CSS_SELECTOR, ".SubmitButton_input__K3jH8").click()

        # confirm we are logged in
        # if self.driver.find_element(By.CSS_SELECTOR, ".username").is_displayed():
        #     # print text of username
        #     if self.driver.find_element(By.CSS_SELECTOR, ".username").text == self.email:
        #         return True
        #     else:
        #         return False

        if self.practice:
            sleep(5)
            # open dropdown menu
            self.driver.find_element(By.CSS_SELECTOR, ".account-menu-header").click()
            # click practice account
            
        


    # search for a 
    def search(self, sb=True, search=None, open=False, close=False, clear=False, verify=False):
        self.stock = search
        self.sb = sb
        self.open = open
        self.close = close
        self.clear = clear
        self.verify = verify

        # open search bar from sidebar
        if self.sb is not False:
            self.driver.find_element(By.CSS_SELECTOR, "div.sidepanel-tab:nth-child(2)").click()

        def clear(self):
            self.driver.find_element(By.CSS_SELECTOR, ".css-115fr6g").clear()

        if self.stock is not None:
            # click search bar and enter stock name or symbol
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/div/div[2]/div[1]").click()
            self.driver.find_element(By.CSS_SELECTOR, ".css-115fr6g").send_keys(self.stock)

        if self.open:
            # select first result
            self.driver.find_element(By.CSS_SELECTOR, "div.search-results-instrument-cell:nth-child(2)").click()

        if self.close:
            self.driver.find_element(By.CSS_SELECTOR, "#app > div.popup-wrapper.popup-opened.active-popup-trading-chart-popup.scale > div > div.popup-content > div > div.trading-chart-layout-header > div.svg-icon-holder.close-button.rectangular").click()

        if self.clear:
            if self.driver.find_element(By.CSS_SELECTOR, ".css-115fr6g").is_displayed():
                self.driver.find_element(By.CSS_SELECTOR, ".css-115fr6g").clear()

        if self.verify:
            if self.verify:
                return True
            else:
                return False


if __name__ == '__main__':
    t = Trading212()
    t.login(practice=True)
    
    

    
    input()
    