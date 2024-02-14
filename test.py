import unittest
from flask import json
from app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        # Setup of resources and configurations needed for the tests - start flask test client
        self.app = app.test_client()
        self.ctx = app.app_context()
        self.ctx.push()

    def tearDown(self):
        # Execute each test regarldess of whether the test passed or failed
        self.ctx.pop()

    def test_get_wikipedia_info_rum(self):
        # User insert "rum", succesful search
        response = self.app.get('/wiki/rum')
        result = json.loads(response.data)
        expected_result = {
            "message": "Search term found",
            "data": "...",
            "Code":   200
        }
        self.assertTrue("message" in result)
        self.assertEqual(result["message"], expected_result["message"])
        self.assertTrue("data" in result)
        self.assertEqual(result["Code"], expected_result["Code"])

    def test_get_wikipedia_info_rumbellion(self):
        # User insert "rumbellion", term found in other article
        response = self.app.get('/wiki/rumbellion')
        result = json.loads(response.data)
        expected_result = {
            "message": "Search term is appeared in other articles",
            "data": "...",
            "Code":   303
        }
        self.assertTrue("message" in result)
        self.assertEqual(result["message"], expected_result["message"])
        self.assertTrue("data" in result)
        self.assertEqual(result["Code"], expected_result["Code"])

    def test_get_wikipedia_info_abcdefgh(self):
        # User insert "abcdefgh", term not found
        response = self.app.get('/wiki/abcdefgh')
        result = json.loads(response.data)
        expected_result = {
            "message": "Search term not found",
            "data": None,
            "Code":   404
        }
        self.assertTrue("message" in result)
        self.assertEqual(result["message"], expected_result["message"])
        self.assertTrue("data" in result)
        self.assertEqual(result["Code"], expected_result["Code"])

    def test_get_wikipedia_info_pi(self):
        # User insert "pi", fuzzy find of term
        response = self.app.get('/wiki/pi')
        result = json.loads(response.data)
        expected_result = {
            "message": "Did you meant",
            "data": "...",
            "Code":   404
        }
        self.assertTrue("message" in result)
        self.assertEqual(result["message"], expected_result["message"])
        self.assertTrue("data" in result)
        self.assertEqual(result["Code"], expected_result["Code"])


if __name__ == '__main__':
    unittest.main()
