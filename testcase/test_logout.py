import unittest
import requests
from lib import load_data
from lib.case_log import case_log_info
from config import config

class TestLogout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file,"退出登录")
    def test_logout_normal(self):
        case_data = load_data.get_case(self.sheet,"test_logout_normal")
        url=case_data[2]
        res=requests.get(url=url)
        case_log_info("test_logout_normal",url,case_data[3],case_data[4],res.text)
        self.assertEqual("<h1>退出登录成功</h1>",res.text)
if __name__=='__main__':
    unittest.main(verbosity=2)