import time
import unittest
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test_case.aiwei_login import aiwei_login
from selenium.webdriver.chrome.options import Options
from test_case.Retryable import retry_on_failure
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class testKnowledge(unittest.TestCase):
    @classmethod
    @retry_on_failure(max_retries=3, delay=1)
    def testsetUpClass(self):
        # 创建 ChromeOptions 实例
        chrome_options = Options()
        # 添加无头模式参数
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chromedriver_path = '/usr/bin/chromedriver'
        # 初始化 WebDriver，传入 ChromeOptions
        service = Service(executable_path=chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        # aiwei_login(self.driver).login()
        self.driver.get("http://aiweinewpre.zizaicloud.cn//login")
        self.driver.maximize_window()
        self.driver.find_element("xpath",
                                 "/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div/input").click()

        self.driver.find_element("xpath",
                                 '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div/input').send_keys(
            "admin87654321")
        self.driver.implicitly_wait(10)
        self.driver.find_element("xpath",
                                 '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div/input').click()
        self.driver.find_element("xpath",
                                 '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div/input').send_keys(
            "WOrkeasy2019.")
        self.driver.find_element("xpath", "//button").click()
        self.driver.find_element("xpath",
                                 '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div[2]/div[2]/span').click()
        # 输入知识名称

        input_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='请输入知识名称']"))
        )
        a = str(random.randint(1, 99999))
        input_element.send_keys("自动化测试知识" + a)
        # 输入标签
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[@class='ivu-tag ivu-tag-size-default ivu-tag-default ivu-tag-checked']//span[contains(text(), '学习资源')]"))
        )
        element.click()
        # 选择类别
        select_element = self.driver.find_element(By.XPATH,
                                                  '//div[@class="ivu-select ivu-select-single ivu-select-default"]//span[contains(text(), "请选择类别")]')
        # print(len(select_element))
        # time.sleep(1000)
        select_element.click()
        internal_share_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ".//li[contains(text(), '内部分享')]"))
        )
        internal_share_option.click()
        # 填写介绍
        textarea_element = self.driver.find_element(By.XPATH, "//textarea[@placeholder='请添加介绍']")
        textarea_element.click()
        textarea_element.send_keys("这是介绍")  # 输入新的文本内容

        # 点击提交按钮
        e = self.driver.find_elements(By.XPATH, "//button[contains(., '确定')]")
        # time.sleep(1000)
        e[13].click()
        time.sleep(1)
        current_url = self.driver.current_url
        # 打印当前页面的URL
        print("新建知识的URL是:", current_url)

        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        # filedir = "/Users/wuwenshuai/Downloads/Dwise/report/pic"
        # if not os.path.exists(filedir):
        #     os.makedirs(filedir)
        # screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        # self.driver.get_screenshot_as_file(screen_name)
        # time.sleep(1111)

        # 定位到含有知识详情的span元素
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'page-title-full-wrapper-left'))
        )

        # 对元素内的文本内容进行断言（去除可能存在的换行符和空格）
        print("知识详情：自动化测试知识"+ a )
        assert "知识详情：自动化测试知识" + a in element.text.strip()


def test_home01(self):
    aiwei_login(self.driver).login()


if __name__ == "__main__":
    unittest.main()
