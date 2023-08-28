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
        self.driver.get("http://aiweinewpre.zizaicloud.cn//login")
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
        time.sleep(2)
        self.driver.find_element("xpath",
                                 "//div[@id='app']/div/div/div/div/ul/li/div").click()
        self.driver.find_element("xpath", "//div[@id='app']/div/div/div/div/ul/li/ul/li").click()
        self.driver.find_element("xpath",
                                 "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr/td[2]/div/div/div/span").click()
        self.driver.find_element("xpath", "//div[3]/div/div/div/div/div/div/div[3]").click()
        time.sleep(1)
        self.driver.find_element("xpath", "//div[3]/div/div/div/div/div/div/div[4]").click()
        time.sleep(1)
        self.driver.find_element("xpath", "//div[3]/div/div/div/div/div/div/div[5]").click()
        self.driver.find_element("xpath", "//li/div").click()
        time.sleep(1)
        self.driver.find_element("xpath", "//li[2]").click()
        self.driver.find_element("xpath",
                                  "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/div/div/span").click()
        time.sleep(5)
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(3)").click()
        # self.driver.execute_script("window.scrollTo(0,0)")
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(4)").click()
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(5)").click()
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(6)").click()
        # self.driver.find_element("Css",
        #                          ".ivu-menu-light > .ivu-menu-submenu:nth-child(1) > .ivu-menu-submenu-title").click()
        # self.driver.find_element("Css", ".ivu-menu-opened .ivu-menu-item:nth-child(3)").click()
        # self.driver.find_element("Css", ".ivu-table-row-hover > .ivu-table-column-11sKh4 span").click()
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(3)").click()
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(4)").click()
        # self.driver.find_element("Css",
        #                          ".ivu-menu-light > .ivu-menu-submenu:nth-child(2) > .ivu-menu-submenu-title").click()
        # self.driver.find_element("Css",
        #                          ".ivu-menu-opened .ivu-menu-submenu:nth-child(1) > .ivu-menu-submenu-title").click()
        # self.driver.find_element("Css", ".ivu-menu-opened > .ivu-menu > .ivu-menu-item:nth-child(1)").click()
        # self.driver.execute_script("window.scrollTo(0,0)")
        # self.driver.find_element("Css", ".ivu-col:nth-child(1) .cardContent:nth-child(3)").click()
        # self.driver.execute_script("window.scrollTo(0,0)")
        # self.driver.execute_script("window.scrollTo(0,0)")
        # self.driver.find_element("Css",
        #                          ".ivu-menu-light > .ivu-menu-submenu:nth-child(2) > .ivu-menu-submenu-title").click()
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(3)").click()
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(4)").click()
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(5)").click()
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(6)").click()
        # self.driver.find_element("Css",
        #                          ".form_row:nth-child(14) > .form_col:nth-child(1) > .show_container").click()
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(7)").click()
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(8)").click()
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(9)").click()
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(10)").click()
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(11)").click()
        # self.driver.find_element("Css", ".ivu-tabs-tab:nth-child(12)").click()

        # @classmethod
        time.sleep(5)

# 打开首页
def test_home01(self):
    time_login(self.driver).login()

if __name__ == "__main__":
    unittest.main()
