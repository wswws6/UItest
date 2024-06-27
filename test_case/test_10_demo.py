import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestTask(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("开始执行测试用例")
        # 设置1
        # 创建 ChromeOptions 实例
        chrome_options = Options()
        # 添加无头模式参数
        chrome_options.add_argument("--headless")
        # 初始化 WebDriver，传入 ChromeOptions
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get("https://www.baidu.com/")

        page_title = cls.driver.title
        print(page_title)
        assert "百度一下" in page_title
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()