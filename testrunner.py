import unittest
import time
import os
from common.HTMLTestRunner import HTMLTestRunner
import os
# 执行case生成报告
# 获取根目录方法
proDir = os.path.abspath(os.path.dirname(__file__)) #根目录地址
# 拼接路径
path = os.path.join(proDir, "report")

class run():
    def runtest(self):
        #\\ 表示表示对\转义 \n \t制表符代表空格
        case_path="/Users/wuwenshuai/Downloads/Dwise/test_case"
        #这个地方需要设置为绝对路径才能正常启动
        test_case = self.Creatsuite(case_path)#所有test自动化用例
        rep = os.path.join(path, "index.html")
        #rep=C:\Users\Administrator\Desktop\Uiframetest\report\index.html
        fp = open(rep, 'wb')
        #定义测试报告
        runner = HTMLTestRunner(stream=fp,title='测试报告',description='执行情况：')

        #运行测试用例
        runner.run(test_case)
        fp.close()  #关闭报告文件

    def Creatsuite(self,case_path):
        suites = unittest.defaultTestLoader.discover(
            start_dir=case_path,
            pattern='test_*.py',
            top_level_dir=None
        )
        return suites

if __name__ == "__main__":
    run().runtest()


