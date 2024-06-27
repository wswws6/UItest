import time
import unittest
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_case.aiwei_login import aiwei_login


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

        # 从包含“生产计划流程”的单元格定位到它所在的td元素
        td_element = production_planning_span.find_element(By.XPATH, "../td")

        # 定位到同一行的第一个日期选择框
        # 假设日期选择框位于td元素下的某个子元素中，并且有特定的标识
        date_input = td_element.find_element(By.XPATH,
                                             ".//div[contains(@class, 'ivu-input') and contains(@class, 'ivu-input-default') and contains(@class, 'ivu-input-with-suffix')]/input")
        # 现在你可以对第一个日期选择框进行操作，例如输入日期
        date_input.click()

        time.sleep(1000)





        # # 输入阶段时间
        # input1 = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-input.ivu-input-default.ivu-input-with-suffix')
        # input1[10].click()
        # # 找到当前日期元素
        # today_element = self.driver.find_elements(By.CLASS_NAME, "ivu-date-picker-cells-cell-today")
        # # 点击当前日期两次
        # today_element[12].click()
        # today_element[12].click()
        # # 输入阶段时间
        # input1 = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-input.ivu-input-default.ivu-input-with-suffix')
        # input1[11].click()
        # # 找到当前日期元素
        # today_element = self.driver.find_elements(By.CLASS_NAME, "ivu-date-picker-cells-cell-today")
        # # 点击当前日期两次
        # today_element[13].click()
        # today_element[13].click()
        # # 输入阶段时间
        # input1 = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-input.ivu-input-default.ivu-input-with-suffix')
        # input1[12].click()
        # # 找到当前日期元素
        # today_element = self.driver.find_elements(By.CLASS_NAME, "ivu-date-picker-cells-cell-today")
        # # 点击当前日期两次
        # today_element[14].click()
        # today_element[14].click()
        # # 输入阶段时间
        # input1 = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-input.ivu-input-default.ivu-input-with-suffix')
        # input1[13].click()
        # # 找到当前日期元素
        # today_element = self.driver.find_elements(By.CLASS_NAME, "ivu-date-picker-cells-cell-today")
        # # 点击当前日期两次
        # today_element[15].click()
        # today_element[15].click()
        # next_step_button = self.driver.find_elements(By.XPATH, "//span[text()='确定']")
        # next_step_button[9].click()
        # # 输入阶段时间
        # time.sleep(1000)


if __name__ == "__main__":
    unittest.main()
