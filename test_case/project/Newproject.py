import os
import time
import unittest
import random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from common.comapi import Common
from public.time_login import time_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




class testShouye(unittest.TestCase):
    @classmethod
    def testsetUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://aiweinewpre.zizaicloud.cn//login")
        # self.driver.maximize_window()

        # self.driver.set_window_size(1724, 1055)
        self.driver.find_element("xpath", "/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div/input").click()

        self.driver.find_element("xpath", '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div/input').send_keys("admin87654321")
        self.driver.implicitly_wait(10)
        self.driver.find_element("xpath", '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div/input').click()
        self.driver.find_element("xpath", '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div/input').send_keys("WOrkeasy2019.")
        self.driver.find_element("xpath", "//button").click()
        self.driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div[1]/div[1]/span').click()
        # 选择项目分类
        # self.driver.find_element("By.CSS_SELECTOR", 'body > div:nth-child(24) > div.ivu-modal-wrap > div > div > div.ivu-modal-body > div > form > div:nth-child(3) > div > div > div.ivu-select-selection > div > span').click()
        # 选择负责人
        time.sleep(2)
        self.driver.find_element("xpath", "/html/body/div[55]/div[2]/div/div/div[2]/div/form/div[8]/form/div/div/div/input").click()
        self.driver.find_element(By.CSS_SELECTOR, 'span[userid="119"]').click()



# 打开首页
def test_home01(self):
    time_login(self.driver).login()

if __name__ == "__main__":
    unittest.main()
