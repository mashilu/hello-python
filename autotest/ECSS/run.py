# -*- coding: utf-8 -*-

import unittest
import os
import time
from autotest.ECSS.library import HTMLTestRunner

timestamp = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime())

discover = unittest.defaultTestLoader.discover("tests", pattern='test_*.py')

report_file = os.path.join(os.getcwd(), 'report', 'Report_' + timestamp + '.html')
fp = open(report_file, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title=u'自动化测试报告',
                                       description=u'用例执行情况')
runner.run(discover)

