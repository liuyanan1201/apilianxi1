import unittest
import requests
from lib import load_data
from lib.case_log import case_log_info
from config import config

class TestGetUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file,"获取用户")

    def test_getuser_normal(self):
        case_data = load_data.get_case(self.sheet,"test_getuser_normal")
        url="http://115.28.108.130:5000/api/user/login/"
        data={"name":"liuliu2","password":"123456"}
        url1=case_data[2]
        session=requests.session()
        session.post(url=url,data=data)
        res=session.get(url=url1)
        case_log_info("test_getuser_normal",case_data[2],case_data[3],case_data[4],res.text)
        print(res.text)
        self.assertIn("用户列表",res.text)

    def test_getuser_logout(self):
        case_data = load_data.get_case(self.sheet,"test_getuser_logout")
        url =case_data[2]
        res=requests.get(url=url)
        case_log_info("test_getuser_logout",url,case_data[3],case_data[4],res.text)
        # print(res.text)
        self.assertEqual("<h1>失败，尚未登录</h1>",res.text)

if __name__=='__main__':
    unittest.main(verbosity=2)