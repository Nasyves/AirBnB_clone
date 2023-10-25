#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from datetime import datetime
import time
from models.review import Review
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    """Test Cases for the Review class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of Review class."""
        
        # Create an instance of the Review class
        b = Review()
        
        # Check the type of the instance
        self.assertEqual(str(type(b)), "<class 'models.review.Review'>")
        
        # Check if the instance is an instance of Review
        self.assertIsInstance(b, Review)
        
        # Check if the instance is a subclass of BaseModel
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Review class."""
        
        # Get the attributes defined for Review class
        attributes = storage.attributes()["Review"]
        
        # Create an instance of Review
        o = Review()
        
        # Check if each attribute exists and has the correct type
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()
