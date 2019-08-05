#coding=utf-8

from readExcel import *
import unittest
import HTMLTestRunner
from sendMail import *

class testMyCase(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def login(self):
        readCase('login')
    
    def addItem(self):
        readCase('addItem')
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

if __name__ == "__main__":
    #定义一个测试套件
    suite = unittest.TestSuite()
    #把测试用例装进套件中
    suite.addTest(testMyCase("login"))
    suite.addTest(testMyCase("addItem"))
    
    import datetime
    t = datetime.datetime.today().strftime("%Y%m%d")

    filename = "testResult_%s.html" % t

    fp = open("./%s.html" % filename, "wb")

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp, title="my first title", description=" test report"
        )

    runner.run(suite)
    fp.close()
    #调用邮件发送模块自动发送测试报告

    sendTestEmail(filename)
    
    
    
    