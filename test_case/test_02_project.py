import time
import unittest
import random
from selenium import webdriver
from test_case.aiwei_login import aiwei_login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from test_case.Retryable import retry_on_failure


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
        radom = str(random.randint(1, 9999999))
        a1[3].send_keys("自动化测试项目"+radom)
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
        # 选择标签
        a = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-default')
        a[0].click()  # 索引10代表第十一个元素
        b = self.driver.find_elements(By.CSS_SELECTOR, 'span.ivu-tag-text.ivu-tag-color-default')
        b[10].click()
        # 点击标签弹窗中的确认
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
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'dpt-title'))
        )
        assert "项目详情：自动化测试项目" + radom in element.text.strip()
        # # 定位到WBStab页
        # wait = WebDriverWait(self.driver, 10)
        # label = self.driver.find_elements(By.CSS_SELECTOR, ".ivu-radio-wrapper.ivu-radio-group-item.ivu-radio-default")
        # label[7].click()

        # # 点击新建按钮
        # button = self.driver.find_element(By.XPATH, "//button[contains(., '新建')]")
        # button.click()
        # # time.sleep(1000)
        # self.driver.quit()

if __name__ == "__main__":
    unittest.main()
