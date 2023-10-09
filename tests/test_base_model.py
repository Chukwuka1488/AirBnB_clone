#!/usr/bin/env python3
"""Test module for BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Class for the test of BaseModel"""

    def setUp(self):
        """Setup for all methods"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def test_attributes(self):
        """Test attributes of BaseModel"""
        self.assertIsInstance(self.base1.id, str)
        self.assertIsInstance(self.base1.created_at, datetime)
        self.assertIsInstance(self.base1.updated_at, datetime)

    def test_str_method(self):
        """Test the __str__ method of BaseModel"""
        expected_str = "[{}] ({}) {}".format(
            self.base1.__class__.__name__, self.base1.id, self.base1.__dict__
        )
        self.assertEqual(str(self.base1), expected_str)

    def test_save(self):
        """Test the save method"""
        pre_change_updated_at = self.base1.updated_at
        self.base1.save()
        post_change_updated_at = self.base1.updated_at
        self.assertNotEqual(pre_change_updated_at, post_change_updated_at)

    def test_to_dict(self):
        """Test conversion of instance to dictionary representation"""
        base1_dict = self.base1.to_dict()
        self.assertEqual(base1_dict["__class__"], "BaseModel")
        self.assertEqual(
            base1_dict["created_at"], self.base1.created_at.isoformat()
        )
        self.assertEqual(
            base1_dict["updated_at"], self.base1.updated_at.isoformat()
        )
        self.assertEqual(base1_dict["id"], self.base1.id)


if __name__ == "__main__":
    unittest.main()
