import unittest

from testcase import test_login

#新建TestSuite
# suite = unittest.TestSuite()
#添加用例
# suite.addTest(TestLogin('test_login_normal'))

#批量添加
# suite.addTests([TestLogin('test_login_normal'),
#                 TestLogin('test_login_password_wrong')])

#添加所有用例 TestLoader测试加载器
#1.遍历所有用例
# suite = unittest.defaultTestLoader.discover(".")

#2.添加模块所有 用例
loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(test_login)

#3.添加类中所有用例
# suite=loader.loadTestsFromTestCase(test_login.TestA)

#4.按名称添加,不需要导入的
# suite = loader.loadTestsFromName("test_login.TestA.test_a")

if __name__=='__main__':
    print(suite)
    print(suite.countTestCases())
    #执行suite
    unittest.TextTestRunner(verbosity=2).run(suite)