import time

class time_login():
    def __init__(self,driver):
        self.driver= driver
    def login(self):
        """// *[ @ id = "app"] / div / div / div[2] / div[2] / div / form / div[1] / div / div[1] / input"""
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/input").send_keys("admin")
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div[1]/input").send_keys("Workeasy2018.")
        time.sleep(2)
        self.driver.find_element_by_css_selector(".ivu-btn.ivu-btn-primary.ivu-btn-long").click()
        time.sleep(2)
