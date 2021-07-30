import unittest
import auth

class TestAuth(unittest.TestCase):
    am = auth.AccountManager("/auth/data/user.db")
    test_user_id = "test_user_id"
    test_truepass = "test_truepass"
    test_wrongpass = "test_wrongpass"
    def test1_signup_success(self):
        self.assertTrue(self.am.signup(test_user_id,test_truepass))
    def test2_signup_fail(self):
        self.assertFalse(self.am.signup(test_user_id,test_truepass))
    def test3_signin_success(self):
        self.assertTrue(self.am.signin(test_user_id,test_truepass))
    def test4_signin_fail(self):
        self.assertFalse(self.am.signin(test_user_id,test_wrongpass))
    def test5_delete_success(self):
        self.assertTrue(self.am.delete_user(test_user_id,test_truepass))
    def test6_delete_fail(self):
        self.assertFalse(self.am.delete_user(test_user_id,test_truepass))

if __name__ == '__main__':
    unittest.main()