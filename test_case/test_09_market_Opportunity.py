import os
import time
import unittest
import random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from common.comapi import Common
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
from public.aiwei_login import aiwei_login
from public.Retryable import retry_on_failure




class market_Opportunity(unittest.TestCase):
    @classmethod
    @retry_on_failure(max_retries=3, delay=1)
    def testsetUpClass(self):
        self.driver = webdriver.Chrome()
        # self.driver.get("http://aiweinewpre.zizaicloud.cn//login")
        aiwei_login(self.driver).login()

        # 定位到包含“市场管理”的标题元素
        sales_opportunity_title = self.driver.find_element("xpath", "//div[@class='ivu-menu-submenu-title' and span[text()='市场管理']]")

        # 展开一级菜单
        sales_opportunity_title.click()
        sales_overview_item = self.driver.find_element("xpath", "//li[@class='ivu-menu-item' and span[text()='市场机会']]")
        sales_overview_item.click()

        # 定位到“新建市场机会”按钮
        button = self.driver.find_element(By.XPATH, "//button[contains(., '新建市场机会')]")
        button.click()
        time.sleep(2)
        # 填写市场机会名称
        radom = str(random.randint(1, 9999999))
        input = self.driver.find_elements(By.CSS_SELECTOR,'.ivu-input.ivu-input-default')
        input[3].send_keys("自动化测试市场机会" + radom)

        # 填写市场机会来源
        a = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-select-placeholder')
        a[1].click()
        time.sleep(1)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(., '促销活动')]"))
        )
        element.click()
        # 选择市场机会时间
        input1 = self.driver.find_elements(By.CSS_SELECTOR,'.ivu-input.ivu-input-default.ivu-input-with-suffix')
        input1[2].click()
        # 找到当前日期元素
        today_element = self.driver.find_elements(By.CLASS_NAME, "ivu-date-picker-cells-cell-today")

        # 点击当前日期两次
        today_element[0].click()
        today_element[0].click()
        # 选择负责人
        input[6].click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, 'span[userid="119"]').click()
        elements = self.driver.find_elements(By.ID, 'task-user-btn')
        elements[0].click()
        # 选择参与人
        input[7].click()
        time.sleep(1)
        b = self.driver.find_elements(By.CSS_SELECTOR, 'span[userid="119"]')
        b[1].click()
        elements[1].click()
        # 填写业务分类
        a = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-select-placeholder')
        a[2].click()
        time.sleep(1)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(., '智能测试业务')]"))
        )
        element.click()
        # 填写预计项目金额
        input = self.driver.find_elements(By.CSS_SELECTOR,'.ivu-input-number-input')
        input[0].send_keys("100")
        # 填写预计项目成交可能性
        input[1].send_keys("50")
        # 填写转化类型
        # time.sleep(1000)
        a11= self.driver.find_elements(By.CSS_SELECTOR, '.ivu-select.ivu-select-single.ivu-select-default')
        print(len(a11))
        a11[7].click()
        # time.sleep(1000)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(., '产品交付')]"))
        )
        element.click()
        # 点击确定
        input = self.driver.find_elements(By.CSS_SELECTOR,'.ivu-btn.ivu-btn-primary')
        input[4].click()
        time.sleep(1)
        current_url = self.driver.current_url
        # 打印当前页面的URL
        print("新建市场机会的URL是:", current_url)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'dpt-title'))
        )
        # print("市场机会详情：自动化测试市场机会"+ radom )
        assert "市场机会详情：自动化测试市场机会" + radom in element.text.strip()

        self.driver.quit()





def test_sales_01(self):
    aiwei_login(self.driver).login()


if __name__ == "__main__":
    unittest.main()
