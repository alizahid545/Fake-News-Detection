#!/usr/bin/env python3
"""
Startup script for Fake News Detection System
"""

import os
import sys
import subprocess
import time

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = [
        'flask', 'scikit-learn', 'pandas', 'numpy', 
        'nltk', 'textblob', 'requests'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Installing missing packages...")
        
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing_packages)
            print("✅ All packages installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to install packages. Please run:")
            print("   pip install -r requirements.txt")
            return False
    
    return True

def download_nltk_data():
    """Download required NLTK data"""
    try:
        import nltk
        
        # Check if punkt tokenizer is available
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            print("📥 Downloading NLTK punkt tokenizer...")
            nltk.download('punkt', quiet=True)
        
        # Check if stopwords are available
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            print("📥 Downloading NLTK stopwords...")
            nltk.download('stopwords', quiet=True)
        
        print("✅ NLTK data ready!")
        return True
        
    except Exception as e:
        print(f"❌ Error downloading NLTK data: {e}")
        return False

def generate_sample_data():
    """Generate sample data if it doesn't exist"""
    if not os.path.exists('expanded_dataset.csv'):
        print("📊 Generating sample dataset...")
        try:
            from data_generator import create_expanded_dataset
            create_expanded_dataset()
        except Exception as e:
            print(f"⚠️  Could not generate sample data: {e}")
            print("   The system will use built-in examples instead.")

def start_server():
    """Start the Flask server"""
    print("\n🚀 Starting Fake News Detection System...")
    print("=" * 50)
    print("📱 Web Interface: http://localhost:5000")
    print("🔧 API Endpoints:")
    print("   - GET  /          : Main interface")
    print("   - POST /predict   : Analyze news")
    print("   - POST /train     : Retrain model")
    print("   - GET  /health    : Health check")
    print("=" * 50)
    print("💡 Press Ctrl+C to stop the server")
    print()
    
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

def main():
    """Main startup function"""
    print("🛡️  Fake News Detection System")
    print("=" * 30)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Download NLTK data
    if not download_nltk_data():
        return
    
    # Generate sample data
    generate_sample_data()
    
    # Start server
    start_server()

if __name__ == "__main__":
    main()
