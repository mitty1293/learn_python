import unittest
from account_manager import AccountManager

class TestAccount(unittest.TestCase):
    am = AccountManager("/auth/data/user.db")
    def test_signup_success(self):
        self.assertTrue(self.am.signup("test1","truepass"))
    def test_signup_fail(self):
        self.assertFalse(self.am.signup("test1","truepass"))
    def test_signin_success(self):
        self.assertTrue(self.am.signin("test1","truepass"))
    def test_signin_fail(self):
        self.assertFalse(self.am.signin("test1","wrongpass"))

if __name__ == '__main__':
    unittest.main()