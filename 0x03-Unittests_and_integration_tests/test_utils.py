#!/usr/bin/env python3
"""
A modoule to test the utils.access_nested_map function
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


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
