import unittest
from config import config
from lib.send_email import send_report
from lib.HTMLTestReportCN import HTMLTestRunner

all=unittest.defaultTestLoader.discover("./testcase")  #发现并收集用例，得到一个测试集合

if __name__=='__main__':
    # unittest.TextTestRunner(verbosity=2).run(suite)
    config.logging.info("测试开始"+"="*50)
    with open(config.report_file,"wb") as f: #二进制写格式 wb
        HTMLTestRunner(stream=f,title="User接口测试报告",description="测试报告").run(all)
    if config.is_send_report:
        send_report()
        config.logging.info("发送邮件成功")
    config.logging.info("测试结束"+"="*50)

