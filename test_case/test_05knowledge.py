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
import datetime


# 104.0.5112.101
class testKnowledge(unittest.TestCase):
    @classmethod
    def testsetUpClass(self):
        self.driver = webdriver.Chrome()  # Linux/macOS示例路径
        # self.driver = webdriver.Chrome()
        self.driver.get("http://aiweinewpre.zizaicloud.cn//login")
        # self.driver.maximize_window()

        # self.driver.set_window_size(1724, 1055)
        self.driver.find_element("xpath",
                                 "/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div/input").click()

        self.driver.find_element("xpath",
                                 '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div/input').send_keys(
            "admin87654321")
        self.driver.implicitly_wait(10)
        self.driver.find_element("xpath",
                                 '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div/input').click()
        self.driver.find_element("xpath",
                                 '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div/input').send_keys(
            "WOrkeasy2019.")
        self.driver.find_element("xpath", "//button").click()
        self.driver.find_element("xpath",
                                 '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div[2]/div[2]/span').click()
        # 输入知识名称
        input_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='请输入知识名称']"))
        )
        input_element.send_keys("知识名称")
        # 输入标签
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[@class='ivu-tag ivu-tag-size-default ivu-tag-default ivu-tag-checked']//span[contains(text(), '学习资源')]"))
        )
        element.click()
        # 选择类别
        select_element = self.driver.find_elements(By.CSS_SELECTOR, ".ivu-select.ivu-select-single.ivu-select-default")
        print(len(select_element))
        print(select_element)
        select_element[11].click()
        internal_share_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ".//li[contains(text(), '内部分享')]"))
        )
        internal_share_option.click()
        # 填写介绍

        textarea_element = self.driver.find_element(By.XPATH, "//textarea[@placeholder='请添加介绍']")
        textarea_element.click()
        textarea_element.send_keys("这是介绍")  # 输入新的文本内容

        e = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-primary')
        e[25].click() # 点击提交按钮
        time.sleep(1111)



def test_home01(self):
    time_login(self.driver).login()


if __name__ == "__main__":
    unittest.main()
