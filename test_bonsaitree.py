# test_bonsaitree.py
"""
Tests for BonsaiTree module.
"""

import unittest
from bonsaitree import BonsaiTree

class TestBonsaiTree(unittest.TestCase):
    """Test cases for BonsaiTree class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BonsaiTree()
        self.assertIsInstance(instance, BonsaiTree)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BonsaiTree()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
