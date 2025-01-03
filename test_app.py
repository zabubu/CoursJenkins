import unittest
from app import app

class TestApp(unittest.TestCase):
    def test_add(self):
        with app.test_client() as client:
            res = client.get('/add?a=3&b=4')
            self.assertEqual(res.json['result'], 7)

if __name__ == '__main__':
    unittest.main()

# modification pour un test Jenkins
