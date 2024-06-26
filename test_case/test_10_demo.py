import os
import time
import unittest
from selenium import webdriver


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
