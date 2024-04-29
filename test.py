import mysql.connector
import random
import unittest
import colorama
import functions as fun

# testing python functions
# TESTING HAS BEEN LIMITED DUE TO LACK OF ACTUAL CONNECTION TO DATABASE until recent update

# copy message for commiting changes.
# git commit -m "[commit message]"

class TestBanking(unittest.TestCase):
    
    def test_account_creation(self):

        result = fun.account_creation()

        self.assertIsNotNone(result)  

if __name__ == '__main__':
    unittest.main()

# FAIL: 