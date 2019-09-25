import os
import unittest
import time
from xwtest.common.sendemail import sendEmail
import BeautifulReport
import os
import sys
current_path=os.path.abspath(os.path.dirname(__file__))
rootpath=os.path.split(current_path)[0]
sys.path.append(rootpath)

#用例路径
case_path=os.path.join(os.getcwd(),'testcase')


def add_case():
    discover=unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)
    return discover

# def run(test_suite):
#
#     #生成测试报告
#     result=BeautifulReport.BeautifulReport(test_suite)
#     fotmat_time=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
#     report_html=f"report{fotmat_time}.html"
#     report_path=os.path.join(os.getcwd(),'report')
#     result.report(description="倩倩测试报告",filename=report_html,report_dir=report_path)
#
#     #发送邮件
#     mailpath=os.path.join(report_path,report_html)
#     sendEmail(mailpath,fotmat_time)
#
#
#
# if __name__ == '__main__':
#     cases=add_case()
#     for case in cases:
#         run(case)





if __name__ == '__main__':
    #生成测试报告
    fotmat_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    report_html = f"report{fotmat_time}.html"
    report_path = os.path.join(os.getcwd(), 'report')
    result=BeautifulReport.BeautifulReport(add_case())
    result.report(description="倩倩测试报告",filename=report_html,report_dir=report_path)

    #发送邮件
    mailpath=os.path.join(report_path,report_html)
    sendEmail(mailpath,fotmat_time)