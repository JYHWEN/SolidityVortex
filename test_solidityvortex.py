# test_solidityvortex.py
"""
Tests for SolidityVortex module.
"""

import unittest
from solidityvortex import SolidityVortex

class TestSolidityVortex(unittest.TestCase):
    """Test cases for SolidityVortex class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityVortex()
        self.assertIsInstance(instance, SolidityVortex)

    def test_run_method(self):
        """Test the run method."""
        instance = SolidityVortex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
