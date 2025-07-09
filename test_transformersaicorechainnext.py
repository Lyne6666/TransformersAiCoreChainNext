# test_transformersaicorechainnext.py
"""
Tests for TransformersAiCoreChainNext module.
"""

import unittest
from transformersaicorechainnext import TransformersAiCoreChainNext

class TestTransformersAiCoreChainNext(unittest.TestCase):
    """Test cases for TransformersAiCoreChainNext class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TransformersAiCoreChainNext()
        self.assertIsInstance(instance, TransformersAiCoreChainNext)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TransformersAiCoreChainNext()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
