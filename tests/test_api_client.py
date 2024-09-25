import unittest, requests
import unittest.mock
from src.api_client import get_location
from unittest.mock import patch

class ApiClientTests(unittest.TestCase):
    
    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'countryName': 'USA', 
            'countryCode': 'US', 
            'timeZone': '-07:00', 
            'zipCode': '94035', 
            'cityName': 'Mou View', 
            'regionName': 'CALI', 
            'isProxy': False, 
            'continent': 'Americas', 
            'continentCode': 'AM', 
            'currency': {
                'code': 'USD', 
                'name': 'US Dollar'
            }, 
            'language': 'English'
        }
        result = get_location("8.8.8.8")
        self.assertEqual(
            result.get("country"), "USA"
        )
        self.assertEqual(
            result.get("region"), "CALI"
        )
        self.assertEqual(
            result.get("city"), "Mou View"
        )
        self.assertEqual(
            result.get("countryCode"), "US"
        )
        self.assertEqual(
            result.get("zipCode"), "94035"
        )
        
        mock_get.assert_called_once_with('http://freeipapi.com/api/json/8.8.8.8')

    @patch('src.api_client.requests.get')
    def test_get_location_returns_side_efect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code = 200,
                json = lambda: {
                    'countryName': 'USA', 
                    'countryCode': 'US', 
                    'timeZone': '-07:00', 
                    'zipCode': '94035', 
                    'cityName': 'Mou View', 
                    'regionName': 'CALI', 
                    'isProxy': False, 
                    'continent': 'Americas', 
                    'continentCode': 'AM', 
                    'currency': {
                        'code': 'USD', 
                        'name': 'US Dollar'
                    }, 
                    'language': 'English'
                }
            )
        ]
    
        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

            result = get_location("8.8.8.8")
            self.assertEqual(
                result.get("country"), "USA"
            )
            self.assertEqual(
                result.get("region"), "CALI"
            )
            self.assertEqual(
                result.get("city"), "Mou View"
            )
            self.assertEqual(
                result.get("countryCode"), "US"
            )
            self.assertEqual(
                result.get("zipCode"), "94035"
            )
            