import os
import random
import sys
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestShouye(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # 创建一个Chrome浏览器驱动对象
        cls.wait = WebDriverWait(cls.driver, 10)  # 创建一个等待对象，等待时间设为10秒
        cls.login()  # 调用login方法进行登录

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # 关闭浏览器驱动对象

    @classmethod
    def login(cls):
        cls.driver.get("http://aiweinewpre.zizaicloud.cn//login")  # 打开登录页面
        cls.driver.maximize_window()  # 最大化浏览器窗口
        cls.driver.find_element(By.XPATH,
                                "/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div/input").click()  # 点击用户名输入框
        cls.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div/input').send_keys(
            "admin87654321")  # 输入用户名
        cls.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div/input').click()  # 点击密码输入框
        cls.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div/input').send_keys(
            "WOrkeasy2019.")  # 输入密码
        cls.driver.find_element(By.XPATH, "//button").click()  # 点击登录按钮
        # cls.wait.until(EC.presence_of_element_located((By.XPATH,
        #                                                '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div[2]/div[1]/span'))).click()  # 等待登录成功页面加载完成

    def test_create_task(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                       '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div[2]/div[1]/span'))).click()  # 等待登录成功页面加载完成
        time.sleep(4)
        task_name_input = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal > .ivu-form .ivu-input")))  # 等待任务名称输入框出现
        task_name_input.click()  # 点击任务名称输入框

        # 生成一个随机数并追加到任务名称中
        random_number = random.randint(1, 100)  # 生成1到100之间的随机数
        input_text = f"自动化测试任务{random_number}"  # 构造任务名称
        task_name_input.send_keys(input_text)  # 输入任务名称

        continue_btn = self.driver.find_element(By.ID, 'task-continue-btn')  # 找到继续按钮
        continue_btn.click()  # 点击继续按钮
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fixed6 .ivu-input"))).click()  # 等待固定元素出现
        time.sleep(1)
        admin_element = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[userid="119"]')))  # 等待管理员元素出现
        admin_element.click()  # 点击管理员元素

        elements = self.driver.find_elements(By.ID, 'task-user-btn')  # 找到任务用户按钮
        if len(elements) >= 4:  # 如果任务用户按钮数量大于等于4
            elements[3].click()  # 点击第四个任务用户按钮
        else:
            print("没有足够的匹配元素来点击第四个。")  # 打印提示信息
        time.sleep(1)
        # 使用JavaScript执行页面滚动到底部的操作
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        tag_button = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-default')
        tag_button[10].click()  # 索引10代表第十一个元素
        tag_button = self.driver.find_elements(By.CSS_SELECTOR, 'span.ivu-tag-text.ivu-tag-color-default')
        tag_button[10].click()
        # 点击标签弹窗中的确认
        # tag_button = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-primary')
        tag_button = self.driver.find_elements(By.XPATH, '//button[@class="ivu-btn ivu-btn-primary" and normalize-space()="确定"]')
        tag_button[22].click()
        print(len(tag_button))

        time.sleep(1)
        # tag_button[29].click()
        # 点击保存或提交按钮完成任务创建
        self.driver.find_element(By.ID, 'task-new-btn').click()

        tag_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.ivu-tag.ivu-tag-size-default.ivu-tag-default.ivu-tag-checked.router-tag'))
        )
        tag_element.click()
        time.sleep(3)
        tag_button = self.driver.find_elements(By.CSS_SELECTOR, '.white-nowrap')
        tag_button[0].click()
        time.sleep(4)
        # button_elements = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-default.ivu-btn-small')
        # if button_elements:
        #     print(len(button_elements))
        #     button_elements[1].click()
        tag_button = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-default.ivu-btn-small')
        tag_button[1].click()

        rating_input_elements = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-input-number-input')
        if rating_input_elements:
            rating_input_elements[1].click()
            rating_input_elements[1].send_keys('8')

        submit_buttons = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-primary')
        if submit_buttons:
            submit_buttons[16].click()
            submit_buttons[16].click()

        screenshot_path = '/Users/wuwenshuai/Downloads/Dwise/report/pic/a.png'
        if os.path.exists(os.path.dirname(screenshot_path)):
            self.driver.save_screenshot(screenshot_path)
        else:
            print("Screenshot directory does not exist.")

            self.driver.quit()

    # 使用示例
    # driver = WebDriver()  # 初始化WebDriver实例
    # task_runner = TaskRunner(driver)
    # task_runner.run_task()

    def tearDown(self):
        time.sleep(2)  # 确保页面元素渲染完成（如果需要的话）

    if __name__ == '__main__':
        unittest.main(testRunner=unittest.TextTestRunner(stream=sys.stdout, verbosity=2), failfast=True)
