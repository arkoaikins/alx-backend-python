#!/usr/bin/env python3
"""
A modoule to test the utils.access_nested_map function
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Testing the utils.access_nested_map function """
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, i, j, expected):
        """Test the access_nested_map."""
        result = access_nested_map(i, j)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, i, j, exception):
        '''test access_nested_map_exception'''
        with self.assertRaises(exception):
            access_nested_map(i, j)


class TestGetJson(unittest.TestCase):
    """ Testing utils.get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """test the json function"""
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Testing memoize function
    """
    def test_memoize(self):
        """test memoize func"""

        class TestClass:
            """test the class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                """testing"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mockod:
            inst = TestClass()
            inst.a_property
            inst.a_property

            mockod.assert_called_once()
