#!/usr/bin/python3
"""Base tests"""
import unittest
from models.base import Base


class BaseTests(unittest.TestCase):
    """tests base"""
    def test_id_count(self):
        """tests if id is working"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_args(self):
        """tests if id is working with args"""
        b1 = Base(8)
        self.assertEqual(b1.id, 8)
