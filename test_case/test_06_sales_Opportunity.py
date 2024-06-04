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




# 104.0.5112.101
class sales_opportunity(unittest.TestCase):
    @classmethod
    @retry_on_failure(max_retries=3, delay=1)
    def testsetUpClass(self):
        self.driver = webdriver.Chrome()
        # self.driver.get("http://aiweinewpre.zizaicloud.cn//login")
        aiwei_login(self.driver).login()

        # 定位到包含“销售机会”的标题元素
        sales_opportunity_title = self.driver.find_element("xpath", "//div[@class='ivu-menu-submenu-title' and span[text()='销售机会']]")

        # 展开一级菜单
        sales_opportunity_title.click()
        sales_overview_item = self.driver.find_element("xpath", "//li[@class='ivu-menu-item' and span[text()='销售机会管理']]")
        sales_overview_item.click()

        # 定位到“新建机会”按钮
        new_opportunity_button = self.driver.find_element(By.XPATH, "//button[contains(., '新建机会')]")
        # 点击“新建机会”按钮
        new_opportunity_button.click()
        # 定位到机会主题输入框
        input_element = self.driver.find_element(By.CSS_SELECTOR, "input.ivu-input[type='text'][maxlength='100']")

        # 点击机会主题输入框
        a = str(random.randint(1, 99999))
        input_element.send_keys("自动化测试销售机会"+ a )
        # 输入测试机会描述
        textarea_element = self.driver.find_element(By.CSS_SELECTOR,
                                               "textarea.ivu-input[style='height: 52px; min-height: 52px; max-height: 115px; overflow-y: hidden;']")
        textarea_element.send_keys("这是一个测试机会描述")

        # 输入成交可能性
        # 根据placeholder定位<input>
        input_element = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='整数']")
        input_element.send_keys("95")
        # 输入预计金额
        input_element = self.driver.find_elements(By.CSS_SELECTOR, ".ivu-input-number-input")
        print(len(input_element))

        input_element[1].click()
        input_element[1].send_keys("10")

        # 点击选择客户
        customer_select = self.driver.find_element(By.CSS_SELECTOR,'body > div:nth-child(40) > div.ivu-modal-wrap > div > div > div.ivu-modal-body > form > div:nth-child(4) > div > div > input')
        customer_select.click()
        time.sleep(2)
        # 选择某个客户
        customer_select = self.driver.find_element(By.XPATH, "//tr[contains(@class, 'ivu-table-row')]//span[.//span[text()='武昌船舶重工集团有限公司']]")
        customer_select.click()
        # 点击客户选择中的确定按钮
        button = self.driver.find_elements(By.CSS_SELECTOR, ".ivu-btn.ivu-btn-primary")
        button[8].click()

        # 选择决策部门 >
        decision_department_select = self.driver.find_elements(By.CSS_SELECTOR, ".ivu-select-input")
        decision_department_select[0].click()
        # 定位到已选中的“采购部”选项，并点击
        purchase_department_option = self.driver.find_element(By.XPATH,
                                                                                "//li[@class='ivu-select-item' and text()='采购部']")
        purchase_department_option.click()

        # 选择一级业务分类
        decision_department_select[1].click()

        purchase_department_option = self.driver.find_elements(By.XPATH,
                                                                                "//li[@class='ivu-select-item' and text()='智能边缘层核心产品']")
        purchase_department_option[0].click()

        # 选择二级业务分类
        decision_department_select[2].click()
        purchase_department_option = self.driver.find_element(By.XPATH,
                                                                                "//li[@class='ivu-select-item' and text()='埃威互联产品']")
        purchase_department_option.click()
        # 选择业务副总
        decision_department_select[3].click()
        purchase_department_option = self.driver.find_element(By.XPATH,
                                                                                "//li[@class='ivu-select-item' and text()='王锐']")
        purchase_department_option.click()
        # 选择销售专家
        decision_department_select[4].click()
        purchase_department_option = self.driver.find_element(By.XPATH,
                                                                                "//li[@class='ivu-select-item' and text()='周雷']")
        purchase_department_option.click()
        # 选择交货状态
        decision_department_select[5].click()
        purchase_department_option = self.driver.find_elements(By.XPATH,
                                                                                "//*[text()='正在交货']")
        purchase_department_option[0].click()
        # 输入机会信息
        textarea_element = self.driver.find_elements(By.CSS_SELECTOR,
                                                    "textarea.ivu-input[style='height: 52px; min-height: 52px; max-height: 115px; overflow-y: hidden;']")
        textarea_element[1].send_keys("这是需求信息")
        # 选择机会负责人
        opportunity_owner = self.driver.find_elements(By.XPATH, '//input[@class="ivu-input ivu-input-default" and @readonly="readonly"]')

        opportunity_owner[1].click()

        b = self.driver.find_element(By.CSS_SELECTOR, 'span[userid="119"]')
        b.click()
        elements = self.driver.find_elements(By.XPATH, "//button[contains(., '确定')]")
        elements[1].click()

        # 选择商务负责人
        opportunity_owner[2].click()
        b = self.driver.find_elements(By.CSS_SELECTOR, 'span[userid="119"]')
        b[1].click()
        elements[2].click()
        # 选择技术负责人
        opportunity_owner[4].click()
        # time.sleep(1000)
        b = self.driver.find_elements(By.CSS_SELECTOR, 'span[userid="119"]')
        b[2].click()
        elements = self.driver.find_elements(By.XPATH, "//button[contains(., '确定')]")
        elements[3].click()
        # 点击确定
        elements = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-primary')
        # time.sleep(1000)
        elements[10].click()
        time.sleep(1)
        current_url = self.driver.current_url
        # 打印当前页面的URL
        print("新建机会的URL是:", current_url)
        # 定位到含有销售机会详情的span元素
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'ivu-breadcrumb-item-link')]"))
        )

        # 对元素内的文本内容进行断言（去除可能存在的换行符和空格）
        # print("销售机会详情：自动化测试销售机会"+a)
        # print(element.text.strip())
        assert "销售机会详情：自动化测试销售机会"+a in element.text.strip()





def test_sales_01(self):
    aiwei_login(self.driver).login()


if __name__ == "__main__":
    unittest.main()
