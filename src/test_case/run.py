#统一入口运行
import unittest
from test_suite import login
#创建一个总的测试套件
suite = unittest.TestSuite()
#将各个测试套件加入到总的测试套件中
suite.addTests(login.return_suite())
#运行测试套件，并生成报告
HTMLReport.TestRunner().run(suite)