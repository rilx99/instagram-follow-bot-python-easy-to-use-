# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from random import choice as rchoice
print ("ins bot by 7rb beta 0.1")
a=raw_input("enter user name:")
lop=int(input("how many account do you put:"))
mylist = open('userandpass.txt').read() .splitlines()
while mylist:
    ch = rchoice(mylist)
    mylist.remove(ch)
    ki9 = ch.rsplit()
    break
class Tg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.instagram.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_tg(self):

        for i in range(lop):
            driver.get("http://clkme.in/qIyaE0")
            time.sleep(12)
            driver.find_element_by_id("skip_button").click()
            while mylist:
                ch = rchoice(mylist)
                mylist.remove(ch)
                ki9 = ch.rsplit()
                driver = self.driver
                driver.get(self.base_url + "/accounts/login/")
                driver.find_element_by_name("username").clear()
                driver.find_element_by_name("username").send_keys(ki9[0])
                driver.find_element_by_name("password").clear()
                driver.find_element_by_name("password").send_keys(ki9[1])
                driver.find_element_by_xpath("//span[@id='react-root']/section/main/div/article/div/div/div/form/span/button").click()
                time.sleep(5)
                driver.get(self.base_url +"/" + a)
                time.sleep(2)
                driver.find_element_by_xpath("//span[@id='react-root']/section/main/article/header/div[2]/div/span/span/button").click()
                driver.get(self.base_url +"/" + a)
                print("done following")
                driver.find_element_by_link_text("Profile").click()
                time.sleep(2)
                driver.find_element_by_xpath("//span[@id='react-root']/section/main/article/header/div[2]/div/div/button").click()
                time.sleep(2)
                driver.find_element_by_css_selector("button._4y3e3").click()
                time.sleep(5)
print("thanks for using instagram bot pls make sure this beta m-a-d-e=b-y=7-r-b")

if __name__ == "__main__":
    unittest.main()
