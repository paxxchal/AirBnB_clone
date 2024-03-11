#!/usr/bin/python3
"""Unit tests for BaseModel class."""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def test_instance_creation(self):
        """Test creation of BaseModel instance."""
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_str_method(self):
        """Test __str__ method."""
        b = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(str(b), expected_str)

    def test_save_method(self):
        """Test save method."""
        b = BaseModel()
        original_updated_at = b.updated_at
        b.save()
        self.assertNotEqual(original_updated_at, b.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method."""
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertIsInstance(b_dict, dict)
        self.assertIn("__class__", b_dict)
        self.assertEqual(b_dict["__class__"], "BaseModel")
        self.assertIn("created_at", b_dict)
        self.assertIn("updated_at", b_dict)
        self.assertEqual(b_dict["created_at"], b.created_at.isoformat())
        self.assertEqual(b_dict["updated_at"], b.updated_at.isoformat())

    # Add more test cases as needed


if __name__ == "__main__":
    unittest.main()
