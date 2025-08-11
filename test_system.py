#!/usr/bin/env python3
"""
Test script for the Fake News Detection System
"""

import requests
import json
import time

def test_system():
    """Test the fake news detection system"""
    
    # Test cases
    test_cases = [
        {
            "name": "Fake News - Miracle Cure",
            "text": "BREAKING: Scientists discover that drinking hot water with lemon cures all diseases instantly! This miracle cure has been hidden by big pharma for years.",
            "expected": "FAKE"
        },
        {
            "name": "Real News - NASA",
            "text": "NASA's Perseverance rover successfully landed on Mars, beginning its mission to search for signs of ancient life.",
            "expected": "REAL"
        },
        {
            "name": "Fake News - Conspiracy",
            "text": "ALIENS CONFIRMED: Government admits to covering up extraterrestrial contact for decades. Shocking new evidence reveals everything.",
            "expected": "FAKE"
        },
        {
            "name": "Real News - Health",
            "text": "The World Health Organization reports that COVID-19 vaccines have been proven safe and effective in clinical trials.",
            "expected": "REAL"
        }
    ]
    
    base_url = "http://localhost:5000"
    
    print("🧪 Testing Fake News Detection System")
    print("=" * 50)
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
        else:
            print("❌ Health check failed")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure the Flask app is running.")
        print("   Run: python app.py")
        return
    
    # Train the model
    print("\n🔄 Training model...")
    try:
        response = requests.post(f"{base_url}/train")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Model trained successfully (Accuracy: {result.get('accuracy', 'N/A'):.2%})")
        else:
            print("❌ Model training failed")
            return
    except Exception as e:
        print(f"❌ Error training model: {e}")
        return
    
    # Test predictions
    print("\n🔍 Testing predictions...")
    correct_predictions = 0
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test_case['name']}")
        print(f"Text: {test_case['text'][:100]}...")
        
        try:
            response = requests.post(
                f"{base_url}/predict",
                json={"text": test_case['text']},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                result = response.json()
                prediction = result.get('prediction', 'UNKNOWN')
                confidence = result.get('confidence', 0)
                
                print(f"Prediction: {prediction} (Confidence: {confidence:.2%})")
                print(f"Expected: {test_case['expected']}")
                
                if prediction == test_case['expected']:
                    print("✅ Correct prediction!")
                    correct_predictions += 1
                else:
                    print("❌ Incorrect prediction")
                    
                # Show detailed results
                print(f"Fake probability: {result.get('fake_probability', 0):.2%}")
                print(f"Real probability: {result.get('real_probability', 0):.2%}")
                
            else:
                print(f"❌ Request failed with status {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error: {e}")
        
        time.sleep(1)  # Small delay between requests
    
    # Summary
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {correct_predictions}/{len(test_cases)} correct predictions")
    accuracy = correct_predictions / len(test_cases) * 100
    print(f"Accuracy: {accuracy:.1f}%")
    
    if accuracy >= 75:
        print("🎉 System is working well!")
    elif accuracy >= 50:
        print("⚠️  System needs improvement")
    else:
        print("❌ System needs significant improvement")

if __name__ == "__main__":
    test_system() 