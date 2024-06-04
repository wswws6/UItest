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
from public.Retryable import retry_on_failure



class testTask(unittest.TestCase):
    @classmethod
    # @retry_on_failure(max_retries=3, delay=1)
    def testsetUpClass(self):
        self.driver = webdriver.Chrome()
        aiwei_login(self.driver).login()
        self.driver.find_element("xpath",
                                 '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div[2]/div[1]/span').click()
        # 定位到任务名称，输入任务名称
        self.driver.find_element(By.CSS_SELECTOR, ".modal > .ivu-form .ivu-input").click()
        # 生成随机数
        random_number = random.randint(1, 100)
        # 使用f-string将随机数转换为字符串并附加到文本后面

        input_text = f"自动化测试任务{random_number}"
        # 找到输入框并发送文本
        self.driver.find_element(By.CSS_SELECTOR, ".modal > .ivu-form .ivu-input").send_keys(input_text)
        # 关闭继续新建
        self.driver.find_element(By.ID, 'task-continue-btn').click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".fixed6 .ivu-input").click()
        time.sleep(2)
        # 选择人员，此时选择的是admin
        self.driver.find_element(By.CSS_SELECTOR, 'span[userid="119"]').click()
        elements = self.driver.find_elements(By.ID, 'task-user-btn')
        if len(elements) >= 4:
            # 点击第四个匹配的元素（索引从0开始）
            elements[3].click()  # 索引1代表第二个元素
        else:
            print("没有足够的匹配元素来点击第四个。")
        # self.driver.find_element(By.CSS_SELECTOR, '.fixed6 .ivu-input').click()
        self.driver.execute_script("window.scrollTo(0,0)")
        # 选择标签
        a = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-default')
        a[10].click()  # 索引10代表第十一个元素

        b = self.driver.find_elements(By.CSS_SELECTOR, 'span.ivu-tag-text.ivu-tag-color-default')
        b[10].click()
        # 点击标签弹窗中的确认
        c = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-primary')
        c[29].click()
        # 发布任务
        self.driver.find_element(By.ID, 'task-new-btn').click()
        time.sleep(2)
        # 获取当前页面的URL
        current_url = self.driver.current_url
        # 打印当前页面的URL
        print("新建任务的URL是:", current_url)
        # self.driver.find_element(By.XPATH, '/html/body/div[22]/div[2]/div/div/div[3]/div/div/button[3]').click()
        # 点击提交任务
        self.driver.find_element(By.CSS_SELECTOR,
                                 "button.dcc_c_margin_left.ivu-btn.ivu-btn-primary.ivu-btn-ghost").click()
        # 点击提交任务弹窗中的确认
        d = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-primary')
        d[7].click()
        # self.driver.find_element(By.CSS_SELECTOR, "button.dcc_c_margin_left.ivu-btn.ivu-btn-primary.ivu-btn-ghost").click()
        time.sleep(1)
        # 点击首页
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.ivu-tag.ivu-tag-size-default.ivu-tag-default.ivu-tag-checked.router-tag').click()
        time.sleep(3)
        # 从首页提醒点击进入任务详情
        e = self.driver.find_elements(By.CSS_SELECTOR, '.white-nowrap')
        e[0].click()
        time.sleep(2)
        # 点击任务提交
        f = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-default.ivu-btn-small')
        # f = self.driver.find_elements(By.XPATH, '//button[@class="ivu-btn ivu-btn-primary" and normalize-space()="确定"]')

        f[1].click()
        # 填写评分
        g = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-input-number-input')
        g[1].click()
        g[1].send_keys('8')
        h = self.driver.find_elements(By.CSS_SELECTOR, '.ivu-btn.ivu-btn-primary')
        h[16].click()
        h[16].click()
        time.sleep(2)
        # 截图
        # self.driver.save_screenshot('/Users/wuwenshuai/Downloads/Dwise/report/pic/a.png')
        # 定位到含有任务详情的span元素
        element = self.driver.find_element(By.XPATH, "//div[@title='Admin 完成任务']")
        actual_text = element.text
        # 假设已经正确获取到实际文本
        time_and_task = actual_text.split(' ')
        if len(time_and_task) >= 3:
            task_text = ' '.join(time_and_task[1:])

            # 移除任务文本首尾及中间可能存在的多余空格
            task_text = ' '.join(task_text.split())
            print(f"实际任务文本为：{task_text}")

            # 验证实际任务文本是否包含 "Admin 完成任务"
            assert "完成任务" == task_text
        else:
            assert False, f"实际文本不包含'完成任务'，实际文本为：{actual_text}"

        time.sleep(2)
        self.driver.quit()


# 打开首页
def test_home01(self):
    aiwei_login(self.driver).login()


if __name__ == "__main__":
    unittest.main()
