# import os
# import time
# import unittest
# import random
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common import keys
# from public.aiwei_login import aiwei_login
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import datetime
# from public.Retryable import retry_on_failure
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-popup-blocking")
# chrome_options.add_argument("--disable-infobars")
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--disable-automation")
# chrome_options.add_argument("--disable-software-rasterizer")
# chrome_options.add_argument("--disable-gpu")
#
#
#
#
# # 104.0.5112.101
# class testproject(unittest.TestCase):
#     @classmethod
#     # @retry_on_failure(max_retries=3, delay=1)
#     def testsetUpClass(self):
#         # 创建一个Chrome浏览器对象并指定禁用自动更新的ChromeOptions
#         self.driver = webdriver.Chrome()
#         aiwei_login(self.driver).login()
#         time.sleep(2)
#
#         self.driver.get("http://aiweinewpre.zizaicloud.cn/detail/project-detail/2286?name=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E9%A1%B9%E7%9B%AE36136")
#         # 定位到WBStab页
#         wait = WebDriverWait(self.driver, 10)
#         label = self.driver.find_elements(By.CSS_SELECTOR, ".ivu-radio-wrapper.ivu-radio-group-item.ivu-radio-default")
#         label[7].click()
#         # 点击新建按钮
#         button = self.driver.find_element(By.XPATH, "//button[contains(., '新建')]")
#         button.click()
#         time.sleep(1)
#
#         # 点击新建阶段按钮
#         button = self.driver.find_element(By.XPATH, "//button[contains(., '阶段')]")
#         button.click()
#         # button= self.driver.find_elements(By.CSS_SELECTOR, '.ivu-input.ivu-input-default')
#         # time.sleep(1)
#         # button[17].send_keys("自动新建阶段")
#         wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(., '阶段名称')]")))
#
#         # 从label元素定位到输入框
#         # 假设输入框位于label元素的父级元素的下一个兄弟元素中
#         input_element = self.driver.find_elements(By.CSS_SELECTOR,
#                                             "div.ivu-form-item-content > div.ivu-input-wrapper.ivu-input-wrapper-default.ivu-input-type-text input.ivu-input.ivu-input-default")
#         print(len(input_element))
#
#         # button= self.driver.find_elements(By.CSS_SELECTOR, '.ivu-input-wrapper.ivu-input-wrapper-default.ivu-input-type-text')
#         time.sleep(1)
#
#         # input_element.click()
#         input_element[5].send_keys("自动新建阶段")
#         # 点击确定
#         input = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-primary')
#         input[14].click()
#         time.sleep(1)
#
#         element = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, '//div[@class="gantt_tree_content"]/div[text()="自动新建阶段"]'))
#         )
#         element.click()
#         # 点击新建任务按钮
#         button = self.driver.find_element(By.XPATH, "//button[contains(., '任务')]")
#         button.click()
#
#         # 输入任务名称
#         input = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-input.ivu-input-default')
#         input[13].send_keys("自动新建任务")
#
#         # 输入预计工时
#         input = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-input-number.ivu-input-number-default')
#         input[1].send_keys("10")
#         # 点击确定
#         # input1 = self.driver.find_elements(By.XPATH, '//button[@class="ivu-btn ivu-btn-primary"]/span[text()="确定"]')
#         #
#         # input1[5].click()
#         # 等待按钮可点击
#         # button = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-primary')
#         # button[13].click()
#
#         button = self.driver.find_elements(By.XPATH, "//button[contains(., '确定')]")
#         button[7].click()
#
#
#         # 点击按钮
#         # time.sleep(1000)
#         self.driver.quit()
#
#
# if __name__ == "__main__":
#     unittest.main()
