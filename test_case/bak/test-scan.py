import time
import time
import unittest
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from public.Retryable import retry_on_failure
from public.aiwei_login import aiwei_login


# 104.0.5112.101
class testproject(unittest.TestCase):
    @classmethod
    # @retry_on_failure(max_retries=3, delay=1)
    def testsetUpClass(self):
        # 创建一个Chrome浏览器对象并指定禁用自动更新的ChromeOptions
        self.driver = webdriver.Chrome()
        aiwei_login(self.driver).login()
        time.sleep(2)

        self.driver.get("http://aiweinewpre.zizaicloud.cn/detail/project-detail/2286?name=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E9%A1%B9%E7%9B%AE36136")
        # 定位到WBStab页
        wait = WebDriverWait(self.driver, 10)
        label = self.driver.find_elements(By.CSS_SELECTOR, ".ivu-radio-wrapper.ivu-radio-group-item.ivu-radio-default")
        label[7].click()
        # 点击新建按钮
        button = self.driver.find_element(By.XPATH, "//button[contains(., '新建')]")
        button.click()
        button = self.driver.find_element(By.XPATH, "//button[contains(., '导入模板')]")
        time.sleep(1)
        button.click()
        # 选择模板
        time.sleep(1)
        element = self.driver.find_element(By.XPATH, "//li[contains(text(), '批产项目')]")
        element.click()
        # 点下一步
        next_step_button = self.driver.find_element(By.XPATH, "//span[text()='下一步']")
        next_step_button.click()
        production_planning_span = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'ivu-table-cell') and contains(., '生产计划流程')]")))


if __name__ == "__main__":
    unittest.main()
