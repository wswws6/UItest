import os
import time
import unittest

from selenium import webdriver

from common.comapi import Common
from public.time_login import time_login


class testShouye(unittest.TestCase):
    @classmethod
    def testsetUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://timetest.cloudepic.cn/login")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    # @classmethod
    # def tearDownClass(self):
    #     # print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
    #     filedir = "D:/test/screenshot/"
    # #
    # if not os.path.exists(filedir):
    #     os.makedirs(filedir)
    # screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
    # self.driver.get_screenshot_as_file(screen_name)
    # self.driver.quit()


# 打开首页
def test_home01(self):
    time_login(self.driver).login()
    HiMessage = Common(self.driver).findElement("Xpath",
                                                "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/span[1]")
    self.assertEqual("Hi 系统管理员，", HiMessage.text)


# def test_home_task(self):
#     # 打开创建任务弹框
#     Common(self.driver).findElement("Xpath",
#                                     "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div/div[1]/div[1]/i").click()
#     time.sleep(2)
#     Common(self.driver).findElement("Xpath",
#                                     "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div/div[2]/ul/li[2]").click()
#     time.sleep(10)
#     # task_tittle=Common(self.driver).findElement("Xpath","/html/body/div[29]/div[2]/div/div/div[1]/div")
#     Common(self.driver).findElement("Xpath",
#                                     "/html/body/div[29]/div[2]/div/div/div[2]/div/div[1]/form[1]/div/div/div[1]/input").sendKeys(
#         "首页任务新建")
    # self.assertEqual("创建任务", task_tittle.text)

if __name__ == "__main__":
    unittest.main()
