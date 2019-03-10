import unittest
import requests
from lib import load_data
from lib.case_log import case_log_info
import json
from config import config

class TestGetToken(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file,"获取token")

    def test_get_token(self):
        case_data = load_data.get_case(self.sheet,"test_get_token")
        url=case_data[2]
        params=json.loads(case_data[3])
        res=requests.get(url=url,params=params)
        case_log_info("test_get_token",url,case_data[3],case_data[4],res.text)
        # print(res.text)
        self.assertIn("token",res.text)
if __name__=="__main__":
    unittest.main(verbosity=2)