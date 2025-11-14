"""
Verification script to check if everything is set up correctly
"""

import sys
import os
from dotenv import load_dotenv

def verify_setup():
    print("🔍 Verifying Capstone Setup...\n")
    
    issues = []
    
    # Check 1: Python version
    print("1️⃣ Checking Python version...")
    if sys.version_info < (3, 8):
        issues.append("❌ Python 3.8+ required")
        print(f"   ❌ Current: {sys.version_info.major}.{sys.version_info.minor}")
    else:
        print(f"   ✅ Python {sys.version_info.major}.{sys.version_info.minor}")
    
    # Check 2: Dependencies
    print("\n2️⃣ Checking dependencies...")
    required_packages = [
        'langchain',
        'langchain_groq',
        'chromadb',
        'sentence_transformers',
        'streamlit',
        'dotenv'
    ]
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"   ✅ {package}")
        except ImportError:
            issues.append(f"❌ Missing package: {package}")
            print(f"   ❌ {package}")
    
    # Check 3: .env file
    print("\n3️⃣ Checking .env file...")
    if not os.path.exists('.env'):
        issues.append("❌ .env file not found")
        print("   ❌ .env file missing")
    else:
        print("   ✅ .env file exists")
        load_dotenv()
        groq_key = os.getenv("GROQ_API_KEY")
        if not groq_key or groq_key == "your_groq_api_key_here":
            issues.append("❌ GROQ_API_KEY not set in .env")
            print("   ⚠️  GROQ_API_KEY not configured")
        else:
            print("   ✅ GROQ_API_KEY configured")
    
    # Check 4: Folder structure
    print("\n4️⃣ Checking folder structure...")
    required_folders = [
        'data',
        'data/announcements',
        'mcp_servers'
    ]
    
    for folder in required_folders:
        if os.path.exists(folder):
            print(f"   ✅ {folder}/")
        else:
            issues.append(f"❌ Missing folder: {folder}")
            print(f"   ❌ {folder}/")
    
    # Summary
    print("\n" + "="*50)
    if issues:
        print("⚠️  SETUP INCOMPLETE")
        print("\nIssues found:")
        for issue in issues:
            print(f"  {issue}")
        print("\nPlease fix the issues above before proceeding.")
    else:
        print("✅ SETUP COMPLETE!")
        print("\nYour environment is ready for Step 2!")
        print("Run: python verify_setup.py anytime to check status.")
    print("="*50)

if __name__ == "__main__":
    verify_setup()