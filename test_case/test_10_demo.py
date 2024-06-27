import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestTask(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
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

    # 打开首页的测试方法
    def test_home01(self):
        # 在这里添加你的测试逻辑
        print("打开首页测试成功")
        pass

if __name__ == "__main__":
    unittest.main()