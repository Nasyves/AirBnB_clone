#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Test Cases for the Amenity class."""

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
        """Tests instantiation of Amenity class."""
        
        # Create an instance of the Amenity class
        b = Amenity()
        
        # Check the type of the instance
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        
        # Check if the instance is an instance of Amenity
        self.assertIsInstance(b, Amenity)
        
        # Check if the instance is a subclass of BaseModel
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Amenity class."""
        
        # Get the attributes defined for Amenity class
        attributes = storage.attributes()["Amenity"]
        
        # Create an instance of Amenity
        o = Amenity()
        
        # Check if each attribute exists and has the correct type
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()
