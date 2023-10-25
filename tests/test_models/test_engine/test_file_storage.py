#!/usr/bin/python3
"""
Test for storage
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.engine.file_storage import FileStorage


class test_fileStorage(unittest.TestCase):
    """Test FileStorage Class"""
    
    def test_instances(self):
        """Checks instantiation of FileStorage class"""
        
        # Create an instance of FileStorage
        obj = FileStorage()
        
        # Check if the instance is an instance of FileStorage
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """Test docstrings"""
        
        # Check if the all method is documented
        self.assertIsNotNone(FileStorage.all.__doc__)
        
        # Check if the new method is documented
        self.assertIsNotNone(FileStorage.new.__doc__)
        
        # Check if the save method is documented
        self.assertIsNotNone(FileStorage.save.__doc__)
        
        # Check if the reload method is documented
        self.assertIsNotNone(FileStorage.reload.__doc__)

if __name__ == '__main__':
    unittest.main()`
