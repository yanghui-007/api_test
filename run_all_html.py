#-*-coding:utf-8-*-
import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
from lib.send_email2 import send_email

#遍历当前目录及子包中所有test*.py中所有unittest用例
#suite=unittest.defaultTestLoader.discover('testcase_umps/productmanagement',pattern='test*.py')
#suite=unittest.defaultTestLoader.discover('testcase_umps/productmanagement',pattern='test*.py')
#suite=unittest.defaultTestLoader.discover('testcase_umps/countryproductlibrary',pattern='test*.py')
suite=unittest.defaultTestLoader.discover('upms_houtai/country_goods',pattern='test*.py')


#1.生成html报告，方法1：
# f=open("report.html","wb")#二进制打开要生成的报告文件
# HTMLTestRunner(stream=f,title="Api Test",description="测试描述").run(suite)
# f.close()

#2.生成html报告，方法2：
with open("report/report.html","wb") as f:#二进制打开要生成的报告文件
    HTMLTestRunner(stream=f,title="Api Test",description="测试描述：本次测试内容为小军美卡系统").run(suite)
    
send_email('report/report.html')#发送邮件