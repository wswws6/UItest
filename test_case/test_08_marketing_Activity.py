import time
import unittest
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test_case.aiwei_login import aiwei_login
from test_case.Retryable import retry_on_failure




# 104.0.5112.101
class marketing_Activity(unittest.TestCase):
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
        sales_overview_item = self.driver.find_element("xpath", "//li[@class='ivu-menu-item' and span[text()='市场活动']]")
        sales_overview_item.click()

        # 定位到“新建市场活动”按钮
        button = self.driver.find_element(By.XPATH, "//button[contains(., '新建市场活动')]")
        button.click()

        # 填写市场活动名称
        radom = str(random.randint(1, 9999999))
        input = self.driver.find_elements(By.CSS_SELECTOR,'.ivu-input.ivu-input-default')
        input[8].send_keys("自动化测试市场活动" + radom)

        # 选择负责人
        input[10].click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, 'span[userid="119"]').click()
        elements = self.driver.find_elements(By.ID, 'task-user-btn')
        elements[0].click()
        # 选择参与人
        input[11].click()
        time.sleep(1)
        b = self.driver.find_elements(By.CSS_SELECTOR, 'span[userid="119"]')
        b[1].click()
        elements[1].click()
        # 点击确定
        input = self.driver.find_elements(By.CSS_SELECTOR,'.ivu-btn.ivu-btn-primary')
        input[6].click()
        time.sleep(1)
        current_url = self.driver.current_url
        time.sleep(1)
        # 打印当前页面的URL
        print("新建市场活动的URL是:", current_url)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'dpt-title'))
        )
        # print("市场活动详情：自动化测试市场活动"+ radom )
        assert "市场活动详情：自动化测试市场活动" + radom in element.text.strip()

        # radio_button = self.driver.find_elements(By.CLASS_NAME, '.ivu-radio-wrapper.ivu-radio-group-item.ivu-radio-default')
        #
        # radio_button[6].click()
        # print(1)
        # time.sleep(1000)
        self.driver.quit()





def test_sales_01(self):
    aiwei_login(self.driver).login()


if __name__ == "__main__":
    unittest.main()
