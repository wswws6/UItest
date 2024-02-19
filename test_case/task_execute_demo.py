import os
import time
import unittest

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
        self.driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div[2]/div[1]/span').click()
        #定位到模态框
        input_element = self.driver.find_element(By.XPATH, '/html/body/div[38]/div[2]/div/div/div[1]')
        # 定位到任务名称，输入任务名称
        self.driver.find_element(By.CSS_SELECTOR, ".modal > .ivu-form .ivu-input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".modal > .ivu-form .ivu-input").send_keys("自动化测试任务")
        # 关闭继续新建
        # self.driver.find_element(By.XPATH,
        #                          '//input[@type="hidden" and @value="true"]').click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".fixed6 .ivu-input").click()

        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, 'span[userid="119"]').click()
        print(1)
        # element = self.driver.find_element(By.XPATH, '//button[@class="ivu-btn ivu-btn-primary"]/span[text()="确定"]')
        # self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element(By.XPATH, '/html/body/div[60]/div[2]/div/div/div[3]/div/div/button[2]').click()
        # self.driver.find_element(By.CSS_SELECTOR, '.fixed6 .ivu-input').click()
        print(3)
        self.driver.execute_script("window.scrollTo(0,0)")
        # 发布任务
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[48]/div[2]/div/div/div[3]/div/div/button[3]/span").click()
        # self.driver.find_element(By.XPATH, '/html/body/div[22]/div[2]/div/div/div[3]/div/div/button[3]').click()
        # print("success")
        self.driver.quit()

# 打开首页
def test_home01(self):
    time_login(self.driver).login()

if __name__ == "__main__":
    unittest.main()
