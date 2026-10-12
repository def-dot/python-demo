"""
标准库unittest

常见断言:
assertEqual/assertNotEqual: 断言两个值是否相等/不相等
assertTrue/assertFalse: 断言值为True/False  
assertIs/assertIsNot: 断言两个对象是否为同一对象/不同对象
assertIn/assertNotIn: 断言一个值是否在另一个值中/不在另一个值中
assertIsInstance/assertNotIsInstance: 断言一个对象是否是某个类的实例/不是某个类的实例  

夹具：
setUp(): 在每个测试方法执行前运行
tearDown(): 在每个测试方法执行后运行
setUpClass(): 在所有测试方法执行前运行一次
tearDownClass(): 在所有测试方法执行后运行一次  
"""


import unittest


def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        # 使用 self.assertEqual 断言结果是否符合预期
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()