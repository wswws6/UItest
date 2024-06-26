import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class testShouye(unittest.TestCase):
    @classmethod
    def testsetUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://aiweinewpre.zizaicloud.cn//login")
        # self.driver.maximize_window()

        # self.driver.set_window_size(1724, 1055)
        self.driver.find_element("xpath", "/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div/input").click()
        #奇怪，登录页的用户名框，css定位不到，xpath就能；seleiuimIDE用xpath就能定位到

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
        time.sleep(2)
        # 选择评价人
        self.driver.find_element(By.CSS_SELECTOR, ".fixed6 .ivu-input").click()
        # self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(2)
        # 搜索评价人
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[60]/div[2]/div/div/div[2]/div/div[1]/div[1]/input").click()
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[60]/div[2]/div/div/div[2]/div/div[1]/div[1]/input").send_keys("Admin")

        # 点击选择评价人
        # self.driver.find_element(By.TAG_NAME,
        #                          "Admin").click()
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[60]/div[2]/div/div/div[2]/div/div[1]/div[2]/ul[14]/li/ul[1]/li/span[2]/span").click()


        # self.driver.find_element("css", '.fixed6 .ivu-input').click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element("xpath",
                                 '/html/body/div[60]/div[2]/div/div/div[3]/div/div/button[2]/span').click()
        # 选择任务标签
        # self.driver.find_element("xpath",
        #                          '/html/body/div[48]/div[2]/div/div/div[2]/div/div[7]/form/div/div/button/span').click()
        # self.driver.find_element("xpath",
        #                          '/html/body/div[62]/div[2]/div/div/div[2]/div[4]/div[1]/div[1]').click()
        # 关闭继续新建
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[48]/div[2]/div/div/div[3]/div/span[1]/span").click()
        # 发布任务
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[48]/div[2]/div/div/div[3]/div/div/button[3]/span").click()
        time.sleep(2)
        print('ok')


        # element = self.driver.find_element("css", ".fixed6 .ivu-input")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).click_and_hold().perform()
        # self.driver.find_element("css", "body").click()
        # self.driver.find_element("xpath",
        #                          "//div[57]/div[2]/div/div/div/div/div/div[2]/ul[7]/li/ul/li/span[2]/span/span/span").click()
        # self.driver.find_element("xpath", "//div[57]/div[2]/div/div/div[2]/div/div[2]/button[2]/span").click()
        # self.driver.find_element("css", ".footer-box:nth-child(2) .ivu-switch").click()
        # self.driver.find_element("xpath",
        #                          "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div/div[1]/div[3]/div/div/section/ol/li/i").click()
        # element = self.driver.find_element("xpath",
        #                                    "//*[@id=\"app\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div/div[1]/div[3]/div/div/section/ol/li/i")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element("css", "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        # self.driver.execute_script("window.scrollTo(0,0)")
        # self.driver.find_element("css", "ol").click()
        # self.driver.find_element("css", ".dot:nth-child(2)").click()
        # self.driver.find_element("css", ".ivu-input-type-textarea:nth-child(2) > .ivu-input").click()
        # self.driver.find_element("css", ".ivu-input-type-textarea:nth-child(2) > .ivu-input").send_keys(
        #     "1、完成了测试")
        # self.driver.find_element("xpath", "//div[2]/input").click()
        # self.driver.find_element("xpath", "//div[2]/input").send_keys("8")
        # self.driver.find_element("css", ".log-modal .ivu-btn:nth-child(2) > span").click()
        # self.driver.find_element("css", ".ivu-avatar-string").click()
        # self.driver.find_element("css", ".ivu-avatar-string").click()
        # self.driver.find_element("css", ".cl_ul_li:nth-child(3)").click()
        # self.driver.find_element("css", ".ivu-btn-text:nth-child(2) > span").click()
        # self.driver.find_element("css", ".ivu-form:nth-child(2) .ivu-input-wrapper > .ivu-input").click()
        # self.driver.find_element("css", ".ivu-form:nth-child(2) .ivu-input-wrapper > .ivu-input").send_keys(
        #     "任务提交备注")
        # self.driver.find_element("css", ".v-transfer-dom:nth-child(25) .ivu-btn-primary > span").click()
        # self.driver.find_element("css", ".detail_content_container").click()
        # self.driver.find_element("css", ".TimelineItem > .ivu-btn:nth-child(2)").click()
        # self.driver.find_element("css", ".ivu-input-number-focused .ivu-input-number-input").click()
        # self.driver.find_element("css", ".ivu-input-number-focused .ivu-input-number-input").send_keys("10")
        # self.driver.find_element("css",
        #                          ".ivu-modal-body > .ivu-form > .ivu-form-item:nth-child(2) .ivu-input").click()
        # self.driver.find_element("css",
        #                          ".ivu-modal-body > .ivu-form > .ivu-form-item:nth-child(2) .ivu-input").send_keys("很好")
        # self.driver.find_element("css", ".foot-container .ivu-btn-primary > span").click()
        # self.driver.find_element("css", ".foot-container .ivu-btn-primary > span").click()
        # self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.quit()

# 打开首页
def test_home01(self):
    time_login(self.driver).login()

if __name__ == "__main__":
    unittest.main()
