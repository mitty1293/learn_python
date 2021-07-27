import unittest
from account_manager import AccountManager

class TestAccount(unittest.TestCase):
    am = AccountManager("/auth/data/user.db")
    test_user_id = "test" + ""
    def test1_signup_success(self):
        self.assertTrue(self.am.signup("test1","truepass"))
    def test2_signup_fail(self):
        self.assertFalse(self.am.signup("test1","truepass"))
    def test3_signin_success(self):
        self.assertTrue(self.am.signin("test1","truepass"))
    def test4_signin_fail(self):
        self.assertFalse(self.am.signin("test1","wrongpass"))
    def test5_delete_success(self):
        self.assertTrue(self.am.delete_user("test1","truepass"))
    def test6_delete_fail(self):
        self.assertFalse(self.am.delete_user("test1","truepass"))

if __name__ == '__main__':
    unittest.main()