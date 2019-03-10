import unittest
import requests
from lib import db
from lib import load_data
import json
from config import config
from lib.case_log import case_log_info

#声明一个测试类,继承unittest.TestCase
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  #整个测试类的测试准备方法
        cls.sheet = load_data.get_sheet(config.data_file,"登录")

    # @unittest.skipUnless(db.check_user("liuliu2"),"跳过该测试用例")#和下面那句话意思相同
    @unittest.skipIf(not db.check_user("liuliu2"), "跳过该测试用例")#如果liuliu2不存在时，跳过该用例
    def test_login_normal(self):  #测试正常登录
        case_data = load_data.get_case(self.sheet,"test_login_normal")
        url=case_data[2]
        data=json.loads(case_data[3])
        res=requests.post(url=url,data=data)
        case_log_info("test_login_normal",url,case_data[3],case_data[4],res.text)

        self.assertEqual(res.text,"<h1>登录成功</h1>")

    def test_login_password_wrong(self): #测试密码错误登录
        case_data = load_data.get_case(self.sheet,"test_login_password_wrong")
        url=case_data[2]
        data=json.loads(case_data[3])
        excepted_res=case_data[4]
        res=requests.post(url=url,data=data)
        case_log_info("test_login_password_wrong",url,case_data[3],case_data[4],res.text)
        self.assertEqual(excepted_res,res.text)


class TestA(unittest.TestCase):
    def test_a(self):
        print("测试")

if __name__ == '__main__':
    unittest.main(verbosity=2)