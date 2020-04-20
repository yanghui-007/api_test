import unittest
import json
import re
import requests
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from lib.get import get_request
from lib.post import post_request
from lib.db2 import *
from lib.HTMLTestReportCN import HTMLTestRunner
from lib.send_email2 import send_email
from test1 import *


suite = unittest.TestLoader().loadTestsFromTestCase(Test_countryproductlibrary)
with open("report/report.html","wb") as f:#二进制打开要生成的报告文件
    HTMLTestRunner(stream=f,title="Api Test",description="测试描述：本次测试内容为小军美卡系统").run(suite)
    
send_email('report/report.html')#发送邮件

# if __name__=='__main__':
#     unittest.main(verbosity=2)