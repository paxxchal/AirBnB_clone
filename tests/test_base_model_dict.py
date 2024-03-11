#!/usr/bin/python3
"""Test case for BaseModel class."""
import unittest
from models.base_model import BaseModel


class TestBaseModelDict(unittest.TestCase):
    """Test cases for BaseModel class with dictionary representation."""

    def test_from_dict_method(self):
        """Test from_dict method."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        my_new_model = BaseModel.from_dict(my_model_json)

        self.assertIsInstance(my_new_model, BaseModel)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)

    # Add more test cases as needed


if __name__ == "__main__":
    unittest.main()
