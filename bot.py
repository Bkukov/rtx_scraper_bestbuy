from selenium import webdriver
from config import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class Bot:

    def __init__(self,k):
        self.keys = k
        self.driver = webdriver.Chrome('./chromedriver')

    def is_sold_out(self):
        try:
            self.driver.find_element_by_xpath(self.keys['add_to_cart']).click()
            time.sleep(2)
            return True
        except:
            return False

    def sign_in(self):
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="header-block"]/div[2]/div[2]/div/nav[2]/ul/li[1]/button/div[2]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="account-menu-app"]/div/div[2]/div/div/a/button').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="fld-e"]').send_keys(self.keys["email"])
            self.driver.find_element_by_xpath('//*[@id="fld-p1"]').send_keys(self.keys["password"])
            self.driver.find_element_by_xpath('/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[4]/button').click()
            time.sleep(4)


    def my_driver(self):

        self.driver.get(self.keys['product_url'])
        self.sign_in()
        am_i_done = False

        while am_i_done == False:

            if self.is_sold_out():

                self.driver.get(self.keys['cart'])
                time.sleep(2)
                self.driver.find_element_by_xpath('//*[@id="cartApp"]/div[2]/div[1]/div/div/span/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button').click()
                time.sleep(2)
                """ uncomment if you're not using best buy card , adds last 3 of credit card linked to best buy"""
                #self.driver.find_element_by_xpath('//*[@id="credit-card-cvv"]').send_keys(self.keys['last_three'])
                """ uncomment in order to press checkout """
                #self.driver.find_element_by_xpath('//*[@id="checkoutApp"]/div/div[1]/div[1]/main/div[2]/div[2]/div/div[5]/div[3]/div/button').click()
                am_i_done = True
            else:
                driver.navigate().refresh();
                time.sleep(2)


        return print('You finally bought a card Bob, congrats nerd.')

if __name__ == '__main__':
    for n in keys:
        my_bot = Bot(keys[n])
        my_bot.my_driver()
