import mysql.connector
import random
import unittest
import colorama
import functions as fun

# testing python functions
# TESTING HAS BEEN LIMITED DUE TO LACK OF ACTUAL CONNECTION TO DATABASE until recent update

class TestBanking(unittest.TestCase):
    
    def test_account_creation(self):

        result = fun.account_creation()

        self.assertIsNotNone(result)  

if __name__ == '__main__':
    unittest.main()

# FAIL: 