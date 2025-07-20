#!/usr/bin/env python3
"""
Simple test suite for Wei-Han Tu's Portfolio Website
"""

import unittest
import tempfile
import os
import sys
from pathlib import Path

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class TestPortfolioApp(unittest.TestCase):
    """Test cases for the portfolio Flask application"""
    
    def setUp(self):
        """Set up test environment"""
        self.app_dir = Path(__file__).parent
        
    def test_required_files_exist(self):
        """Test that all required files exist"""
        required_files = [
            'app.py',
            'requirements.txt',
            'static/index.html',
            'README.md',
            'LICENSE.txt',
            '.gitignore'
        ]
        
        for file in required_files:
            with self.subTest(file=file):
                self.assertTrue(
                    (self.app_dir / file).exists(),
                    f"Required file {file} does not exist"
                )
    
    def test_flask_app_import(self):
        """Test that Flask app can be imported"""
        try:
            from app import app
            self.assertIsNotNone(app)
        except ImportError as e:
            self.fail(f"Failed to import Flask app: {e}")
    
    def test_static_files_exist(self):
        """Test that static files exist"""
        static_files = [
            'static/index.html',
            'static/assets/css/main.css',
            'static/assets/js/main.js'
        ]
        
        for file in static_files:
            with self.subTest(file=file):
                self.assertTrue(
                    (self.app_dir / file).exists(),
                    f"Static file {file} does not exist"
                )
    
    def test_html_content(self):
        """Test that HTML file contains expected content"""
        html_file = self.app_dir / 'static' / 'index.html'
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check for essential elements
        self.assertIn('Wei-Han Tu', content)
        self.assertIn('Portfolio', content)
        self.assertIn('GitHub', content)
        self.assertIn('Contact', content)
    
    def test_requirements_format(self):
        """Test that requirements.txt has correct format"""
        req_file = self.app_dir / 'requirements.txt'
        
        with open(req_file, 'r') as f:
            lines = f.readlines()
            
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                # Check if line has package==version format
                self.assertIn('==', line, f"Invalid requirement format: {line}")

def run_tests():
    """Run all tests"""
    print("🧪 Running portfolio tests...")
    print("=" * 50)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestPortfolioApp)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("=" * 50)
    if result.wasSuccessful():
        print("✅ All tests passed!")
        return True
    else:
        print("❌ Some tests failed!")
        return False

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1) 