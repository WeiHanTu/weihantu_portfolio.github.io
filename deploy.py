#!/usr/bin/env python3
"""
Deployment script for Wei-Han Tu's Portfolio Website
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'requirements.txt',
        'static/index.html',
        'README.md',
        'LICENSE.txt',
        '.gitignore'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    
    print("✅ All required files found")
    return True

def run_tests():
    """Run basic tests"""
    try:
        # Test Flask app import
        result = subprocess.run([
            sys.executable, '-c', 
            'from app import app; print("Flask app imported successfully")'
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Flask app test passed")
            return True
        else:
            print(f"❌ Flask app test failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def check_git_status():
    """Check git status"""
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True)
        
        if result.stdout.strip():
            print("⚠️  Uncommitted changes detected")
            print(result.stdout)
            return False
        else:
            print("✅ Git repository is clean")
            return True
            
    except Exception as e:
        print(f"❌ Git check failed: {e}")
        return False

def deploy():
    """Main deployment function"""
    print("🚀 Starting portfolio deployment...")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        return False
    
    # Run tests
    if not run_tests():
        return False
    
    # Check git status
    if not check_git_status():
        print("💡 Consider committing changes before deploying")
    
    print("=" * 50)
    print("✅ Deployment checks completed successfully!")
    print("\n📋 Next steps:")
    print("1. Commit your changes: git add . && git commit -m 'Update portfolio'")
    print("2. Push to GitHub: git push origin main")
    print("3. GitHub Actions will automatically deploy to GitHub Pages")
    print("4. Your portfolio will be available at: https://weihantu.github.io/weihantu_portfolio.github.io")
    
    return True

if __name__ == "__main__":
    success = deploy()
    sys.exit(0 if success else 1) 