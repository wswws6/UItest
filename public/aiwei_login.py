import time

class aiwei_login():
    def __init__(self,driver):
        self.driver= driver
    def login(self):
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