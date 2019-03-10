import unittest
import json
import requests
from lib.case_log import case_log_info
from lib.db import check_user,delete_user
from lib import load_data
from config import config

class TestReg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file,"注册")
    def test_reg_normal(self):
        case_data=load_data.get_case(self.sheet,"test_reg_normal")
        NAME="test100"
        if check_user(NAME):
            delete_user(NAME)
        url=case_data[2]
        try:
            data=json.loads(case_data[3])
            excepted_res=json.loads(case_data[4])
        except json.decoder.JSONDecodeError as e:
            config.logging.error("用例数据不是合法json")

        res=requests.post(url=url,json=data)
        case_log_info("test_reg_normal",url,case_data[3],case_data[4],res.text)

        try:
            res_json=res.json()
        except json.decoder.JSONDecodeError as e:
            config.logging.error("返回结果不是json格式")

        self.assertDictEqual(excepted_res,res.json())

        delete_user("test100")

    def  test_reg_exit(self):
        case_data = load_data.get_case(self.sheet,"test_reg_exit")
        url=case_data[2]
        data=json.loads(case_data[3])
        excepted_res=json.loads(case_data[4])
        res=requests.post(url=url,json=data)
        case_log_info("test_reg_exit",url,case_data[3],case_data[4],res.text)
        self.assertDictEqual(excepted_res,res.json())


if __name__ == '__main__':
    unittest.main(verbosity=2)
