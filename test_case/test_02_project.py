import os
import time
import unittest
import random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from common.comapi import Common
from public.aiwei_login import aiwei_login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
from public.Retryable import retry_on_failure


# 104.0.5112.101
class testproject(unittest.TestCase):
    @classmethod
    @retry_on_failure(max_retries=3, delay=1)
    def testsetUpClass(self):
        self.driver = webdriver.Chrome()  # Linux/macOS示例路径
        aiwei_login(self.driver).login()
        self.driver.find_element("xpath",
                                 '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div[1]/div[1]/span').click()
        # 选择项目分类
        a = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-select-placeholder')
        a[0].click()
        time.sleep(1)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(., 'E-部门职能')]"))
        )
        element.click()
        # 获取当前时间
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print(current_time)
        # 选择项目代号
        a1 = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-form-item-content > .ivu-input-wrapper-default.ivu-input-type-text > .ivu-input')
        # 填写项目代号
        a1[2].send_keys("auto"+str(random.randint(1, 9999999999)))
        # 填写项目名称
        a1[3].send_keys("自动化测试项目"+str(random.randint(1, 99999)))
        # 选择负责人
        a1[4].click()
        self.driver.find_element(By.CSS_SELECTOR, 'span[userid="119"]').click()
        elements = self.driver.find_elements(By.ID, 'task-user-btn')
        time.sleep(1)
        elements[2].click()
        # 选择参与人
        a1[5].click()
        time.sleep(1)
        b = self.driver.find_elements(By.CSS_SELECTOR, 'span[userid="119"]')
        b[1].click()
        elements = self.driver.find_elements(By.ID, 'task-user-btn')
        elements[3].click()
        #选择标签
        a = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-default')
        a[0].click()  # 索引10代表第十一个元素
        b = self.driver.find_elements(By.CSS_SELECTOR, 'span.ivu-tag-text.ivu-tag-color-default')
        b[10].click()
        #点击标签弹窗中的确认
        c = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-primary')
        c[30].click()
        # 点击下一步
        c = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-primary')
        c[4].click()
        # 点击跳过导入WBS
        c = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-default')
        c[1].click()

        # self.driver.find_element(By.XPATH, '/html/body/div[22]/div[2]/div/div/div[3]/div/div/button[3]').click()
        time.sleep(1)
        current_url = self.driver.current_url
        # 打印当前页面的URL
        print("新建项目的URL是:", current_url)
        # # 点击挂起
        # d = self.driver.find_elements(By.CSS_SELECTOR, '.margin_left_small.ivu-btn.ivu-btn-text.ivu-btn-small')
        # d[3].click()
        # e = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-primary')
        # time.sleep(11111)
        # e[22].click()
        # # 点击重启
        # d = self.driver.find_elements(By.CSS_SELECTOR, '.margin_left_small.ivu-btn.ivu-btn-text.ivu-btn-small')
        #
        # d[3].click()
        # e = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-primary')
        # print(e)
        # time.sleep(1)
        # e[22].click()
        #
        #
        # time.sleep(10000)
        # 打开首页


if __name__ == "__main__":
    unittest.main()
