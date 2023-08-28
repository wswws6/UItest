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
        self.driver.get("http://aiweinewtest.zizaicloud.cn//login")
        self.driver.implicitly_wait(100)
        # self.driver.set_window_size(1724, 1055)
        self.driver.find_element("xpath", "/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div/input").click()
        #奇怪，登录页的用户名框，css定位不到，xpath就能；seleiuimIDE用xpath就能定位到
        # self.driver.find_element("Css",
        #                          '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div/input').click()

        self.driver.find_element("xpath", '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div/input').send_keys("admin87654321")
        self.driver.implicitly_wait(10)
        self.driver.find_element("xpath", '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div/input').click()
        self.driver.find_element("xpath", '/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div/input').send_keys("WOrkeasy2019.")
        self.driver.find_element("xpath", "//button").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element("Css",
                                 ".ivu-menu-light > .ivu-menu-submenu:nth-child(1) > .ivu-menu-submenu-title").click()
        self.driver.find_element("Css", ".ivu-menu-opened .ivu-menu-item:nth-child(1)").click()
        self.driver.find_element("Css",
                                 ".ivu-table-row-hover > .ivu-table-column-DZSvnp .ivu-table-cell-tooltip-content").click()

        time.sleep(5)
    # @classmethod


# 打开首页
def test_home01(self):
    time_login(self.driver).login()

if __name__ == "__main__":
    unittest.main()


