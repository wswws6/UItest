class Common():
    def __init__(self, driver):
        self.driver = driver

    #定义了一个方法，传入两个行参
    def findElement(self,byWay,wayAttribute):
        if byWay == 'ID':
            return self.driver.find_element_by_id(wayAttribute)
        elif byWay == 'Xpath':
            return self.driver.find_element_by_xpath(wayAttribute)
        elif byWay == 'Xname':
            return self.driver.find_element_by_name(wayAttribute)
        elif byWay == 'Css':
            return self.driver.find_element_by_css_selector(wayAttribute)
        elif byWay == 'LinkText':
            return self.driver.find_element_by_link_text(wayAttribute)
        elif byWay == 'ClassName':
            return self.driver.find_element_by_class_name(wayAttribute)
        elif byWay == 'Clcs':
            return self.driver.find_elements_by_class_name(wayAttribute)



















