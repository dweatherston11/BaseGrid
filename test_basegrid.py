# test_basegrid.py
"""
Tests for BaseGrid module.
"""

import unittest
from basegrid import BaseGrid

class TestBaseGrid(unittest.TestCase):
    """Test cases for BaseGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BaseGrid()
        self.assertIsInstance(instance, BaseGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BaseGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
