import os
import time
import unittest
import random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from public.aiwei_login import aiwei_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from public.Retryable import retry_on_failure



class testTask(unittest.TestCase):
    @classmethod
    # @retry_on_failure(max_retries=3, delay=1)
    def testsetUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")

        page_title = self.driver.title
        print(page_title)
        time.sleep(2)



# 打开首页
def test_home01(self):
    aiwei_login(self.driver).login()


if __name__ == "__main__":
    unittest.main()
