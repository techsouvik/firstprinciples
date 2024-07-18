import unittest
import requests

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://auth-service:5000"

    def test_signup(self):
        response = requests.post(f"{self.base_url}/signup", json={'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)

    def test_signin(self):
        self.test_signup()
        response = requests.post(f"{self.base_url}/signin", json={'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
