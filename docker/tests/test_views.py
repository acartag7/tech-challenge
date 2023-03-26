'''Tests for the views module.'''
import unittest
import json  # Import json module
from app import app

class TestViews(unittest.TestCase):
    '''Tests for the views module.'''
    def setUp(self):
        self.app = app.test_client()

    def test_encode_valid_input(self):
        '''Test that the encode view returns the correct result for a valid input.'''
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'result': 'mjqqt'})

    def test_encode_invalid_input(self):
        '''Test that the encode view returns the correct result for an invalid input.'''
        response = self.app.get('/hello!')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.get_json(),
            {'error': 'Input must contain only alphanumeric characters.'}
        )

    def test_encode_empty_input(self):
        '''Test that the encode view returns the correct result for an empty input.'''
        response = self.app.get('/')
        self.assertEqual(response.status_code, 404)

    def test_encode_numeric_input(self):
        '''Test that the encode view returns the correct result for a numeric input.'''
        response = self.app.get('/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data()), {'result': '67890'})

    def test_status(self):
        '''Test that the status view returns the correct result.'''
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'status': 'ok'})

    def test_help(self):
        '''Test that the help view returns the correct result.'''
        response = self.app.get('/help')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<h1>Instructions</h1>', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
