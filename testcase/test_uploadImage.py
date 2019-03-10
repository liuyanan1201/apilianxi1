import unittest
import requests
from lib import load_data
from lib.case_log import case_log_info
import json
from config import config

class TestUpload(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file,"上传文件")

    def test_uploadimage_normal(self):
        case_data = load_data.get_case(self.sheet,"test_uploadimage_normal")
        url=case_data[2]
        # f=open("1.txt")
        files =json.loads(case_data[3])
        res=requests.post(url=url,files=files)
        case_log_info("test_uploadimage_normal",url,case_data[3],case_data[4],res.text)
        # print(res.text)
        self.assertEqual("<h1>上传成功</h1>",res.text)
if __name__=='__main__':
    unittest.main(verbosity=2)
