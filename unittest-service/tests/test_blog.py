import unittest
import requests

class BlogTestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://blog-service:5001"

    def test_create_post(self):
        response = requests.post(f"{self.base_url}/posts", json={'title': 'Test Post', 'content': 'This is a test post', 'author': 'testuser'})
        self.assertEqual(response.status_code, 200)

    def test_get_posts(self):
        response = requests.get(f"{self.base_url}/posts")
        self.assertEqual(response.status_code, 200)

    def test_get_post(self):
        response = requests.get(f"{self.base_url}/posts/1")
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
