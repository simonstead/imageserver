import unittest
from app import app

class ImageServerTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index(self):
        r = self.app.get('/')
        self.assertEqual(r.status_code, 200, 'expected 200 response code')

    def test_images(self):
        r = self.app.get('/images/test.png')
        self.assertEqual(r.status_code, 200, 'expected 200 response code')

