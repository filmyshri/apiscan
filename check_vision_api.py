#!/usr/bin/env python3
"""
Google Vision API Configuration Checker
Verifies if the Google Vision API is properly configured
"""

import os
import json
import sys
from pathlib import Path

def check_credentials():
    """Check if credentials are configured"""
    print("🔍 Checking Google Vision API Configuration...\n")
    
    # Check for credentials.json
    creds_path = Path("credentials.json")
    
    if creds_path.exists():
        print("✅ credentials.json found")
        
        # Validate JSON format
        try:
            with open(creds_path) as f:
                creds = json.load(f)
                
            # Check required fields
            required_fields = ['type', 'project_id', 'private_key', 'client_email']
            for field in required_fields:
                if field in creds:
                    print(f"  ✅ {field}: OK")
                else:
                    print(f"  ❌ {field}: MISSING")
                    return False
            
            print(f"\n📊 Service Account Details:")
            print(f"  Project ID: {creds.get('project_id')}")
            print(f"  Email: {creds.get('client_email')}")
            
        except json.JSONDecodeError:
            print("❌ credentials.json is invalid JSON format")
            return False
    else:
        print("❌ credentials.json not found")
        print("\n📝 To fix this:")
        print("  1. Download credentials from Google Cloud Console")
        print("  2. Place the JSON file in the project directory")
        print("  3. Name it 'credentials.json'")
        return False
    
    # Try importing and testing
    print("\n🧪 Testing Google Vision API import...")
    try:
        from google.cloud import vision
        print("✅ google-cloud-vision library imported successfully")
        
        # Try creating client
        try:
            client = vision.ImageAnnotatorClient.from_service_account_file(str(creds_path))
            print("✅ Vision API client created successfully")
            print(f"   Project: {client.project_id if hasattr(client, 'project_id') else 'N/A'}")
            return True
        except Exception as e:
            print(f"❌ Failed to create Vision API client: {e}")
            return False
            
    except ImportError:
        print("❌ google-cloud-vision not installed")
        print("   Install with: pip install google-cloud-vision")
        return False

if __name__ == "__main__":
    success = check_credentials()
    
    if success:
        print("\n" + "="*50)
        print("✅ Google Vision API is properly configured!")
        print("="*50)
        sys.exit(0)
    else:
        print("\n" + "="*50)
        print("❌ Google Vision API is NOT configured")
        print("="*50)
        print("\nSee GOOGLE_VISION_SETUP.md for detailed instructions")
        sys.exit(1)
