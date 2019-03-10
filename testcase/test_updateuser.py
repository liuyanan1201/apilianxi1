import unittest
import requests
from lib import load_data
from lib.case_log import case_log_info
import json
from config import config

class TestUpdateUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file,"更新用户")

    def test_update_user(self):
        case_data = load_data.get_case(self.sheet,"test_update_user")
        url=case_data[2]
        data=json.loads(case_data[3])
        excepted_res = json.loads(case_data[4])
        res=requests.post(url=url,json=data)
        case_log_info("test_update_user",url,case_data[3],case_data[4],res.text)
        self.assertDictEqual(excepted_res,res.json())
        # print(res.text)
        # self.assertEqual("100000",res.json()["code"])
        # self.assertEqual("成功",res.json()["msg"])
        # self.assertEqual("liuliu2",res.json()["data"]["name"])

if __name__=='__main__':
    unittest.main(verbosity=2)