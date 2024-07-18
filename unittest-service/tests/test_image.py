import unittest
import requests
from io import BytesIO

class ImageServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://image-service:5002"

    def test_upload_image(self):
        files = {
            'file': ('test.jpg', BytesIO(b'test image content'), 'image/jpeg')
        }
        response = requests.post(f"{self.base_url}/upload", files=files)
        self.assertEqual(response.status_code, 200)

    def test_get_image(self):
        response = requests.get(f"{self.base_url}/images/test.jpg")
        self.assertEqual(response.status_code, 404)  # Assuming the image hasn't been uploaded in this isolated test.

if __name__ == '__main__':
    unittest.main()
