import unittest
from app import app
from app.views import Administrator


class Test_Signup(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def Test_User_registration(self):
        with app.test_client as client:
            test_user = client.post("/app/v1/auth/signup", data ={"username":"farooq", "password":"araali", "confirm_password":"araali"}) 
            self.assertEqual(test_user.status_code,201)
            


if __name__=='__main__':
    unittest.main()		