
#数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user ='test'
db_password = '123456'
db = 'api_test'


#路径配置
import os
# config_path=os.path.abspath(__file__)
# config_path1=os.path.dirname(config_path)
# project_path=os.path.dirname(config_path1)
#项目目录
project_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#数据文件目录
# data_path=os.path.join(project_path,'data')
data_file=os.path.join(project_path,'data','data.xls')

#日志文件目录
log_file = os.path.join(project_path,'log','log.txt')

#报告文件目录
report_file = os.path.join(project_path,'report','report.html')


#log配置
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file,
                    filemode="w")#a是追加模式 不写时默认是追加模式  w是覆盖模式
if __name__=='__main__':
    # logging.info("hello world")
    # logging.info("你好")
    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print(data_file)
    print(log_file)
    print(report_file)


#邮件配置
smtp_server='smtp.126.com'
smtp_user= 'liuyn120731@126.com'
smtp_password='liuyanan123'

receiver=['694526779@qq.com','15910457235@163.com']
subject='接口测试报告'
body='hi,all,\n附件中是接口测试报告，请查收'

is_send_report=True  #不发送邮件