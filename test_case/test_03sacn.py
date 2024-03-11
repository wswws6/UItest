import os
import time
import unittest

from selenium import webdriver

from common.comapi import Common
from public.aiwei_login import aiwei_login
from public.Retryable import retry_on_failure



class testShouye(unittest.TestCase):
    @classmethod
    @retry_on_failure(max_retries=3, delay=1)
    def testsetUpClass(self):
        self.driver = webdriver.Chrome()
        aiwei_login(self.driver).login()
        self.driver.implicitly_wait(10)
        time.sleep(2)
        self.driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div[1]/div/ul/li[1]/div').click()
        time.sleep(2)
        self.driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[1]/div/ul/li[2]/div').click()
        time.sleep(2)

# 打开首页
def test_home01(self):
    aiwei_login(self.driver).login()

if __name__ == "__main__":
    unittest.main()
