#!/usr/bin/env python3
"""
Unit tests for Assignment 1
"""

import unittest
from assignment1 import greet


class TestAssignment1(unittest.TestCase):
    """Test cases for assignment1.py"""
    
    def test_greet_with_name(self):
        """Test greeting with a specific name"""
        result = greet("Alice")
        self.assertEqual(result, "Hello, Alice!")
    
    def test_greet_with_world(self):
        """Test greeting with World"""
        result = greet("World")
        self.assertEqual(result, "Hello, World!")
    
    def test_greet_with_empty_string(self):
        """Test greeting with empty string"""
        result = greet("")
        self.assertEqual(result, "Hello, !")
    
    def test_greet_with_non_string(self):
        """Test greeting with non-string input raises TypeError"""
        with self.assertRaises(TypeError):
            greet(123)
        with self.assertRaises(TypeError):
            greet(None)


if __name__ == "__main__":
    unittest.main()
