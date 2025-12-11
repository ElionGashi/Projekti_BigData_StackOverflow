"""
Unit tests for utility functions
"""
import unittest
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from utils.config import PROJECT_ROOT, DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR


class TestConfig(unittest.TestCase):
    """Test configuration settings"""
    
    def test_project_root_exists(self):
        """Test that project root directory exists"""
        self.assertTrue(PROJECT_ROOT.exists())
    
    def test_data_directories_exist(self):
        """Test that data directories exist"""
        self.assertTrue(DATA_DIR.exists())
        self.assertTrue(RAW_DATA_DIR.exists())
        self.assertTrue(PROCESSED_DATA_DIR.exists())
    
    def test_directories_are_paths(self):
        """Test that directory variables are Path objects"""
        self.assertIsInstance(PROJECT_ROOT, Path)
        self.assertIsInstance(DATA_DIR, Path)


class TestLogger(unittest.TestCase):
    """Test logging functionality"""
    
    def test_logger_creation(self):
        """Test that logger can be created"""
        from utils.logger import setup_logger
        
        logger = setup_logger("test_logger")
        self.assertIsNotNone(logger)
        self.assertEqual(logger.name, "test_logger")


if __name__ == '__main__':
    unittest.main()
