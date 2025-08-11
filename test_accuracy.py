#!/usr/bin/env python3
"""
Test script to demonstrate fake news detection accuracy
Shows the system can distinguish between fake and real news
"""

import requests
import json

def test_news_article(text, expected_type):
    """Test a news article and show results"""
    try:
        response = requests.post(
            'http://localhost:5000/predict',
            json={'text': text},
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            result = response.json()
            prediction = result.get('prediction', 'UNKNOWN')
            confidence = result.get('confidence', 0)
            fake_prob = result.get('fake_probability', 0)
            real_prob = result.get('real_probability', 0)
            
            print(f"📰 Test: {expected_type}")
            print(f"   Text: {text[:80]}...")
            print(f"   Prediction: {prediction}")
            print(f"   Confidence: {confidence:.1%}")
            print(f"   Fake Probability: {fake_prob:.1%}")
            print(f"   Real Probability: {real_prob:.1%}")
            
            # Check if prediction matches expected
            if prediction == expected_type:
                print(f"   ✅ CORRECT - System correctly identified as {expected_type}")
            else:
                print(f"   ❌ INCORRECT - Expected {expected_type}, got {prediction}")
            
            print("-" * 60)
            return prediction == expected_type
        else:
            print(f"❌ Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing: {e}")
        return False

def main():
    """Test various news articles"""
    print("🛡️ Fake News Detection System - Accuracy Test")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        # Fake news examples
        {
            "text": "BREAKING: Scientists discover that drinking hot water with lemon cures all diseases instantly! This miracle cure has been hidden by big pharma for years.",
            "expected": "FAKE"
        },
        {
            "text": "ALIENS CONFIRMED: Government admits to covering up extraterrestrial contact for decades. Shocking new evidence reveals everything.",
            "expected": "FAKE"
        },
        {
            "text": "5G CAUSES COVID: New study proves that 5G networks are responsible for the coronavirus pandemic. Experts say radiation is the real culprit.",
            "expected": "FAKE"
        },
        {
            "text": "FLAT EARTH PROVEN: NASA finally admits the Earth is flat after pressure from social media. All space photos were CGI.",
            "expected": "FAKE"
        },
        {
            "text": "TIME TRAVEL ACHIEVED: Scientists successfully send a cat back to 1920. The cat returned with a message from the past.",
            "expected": "FAKE"
        },
        
        # Real news examples
        {
            "text": "NASA's Perseverance rover successfully landed on Mars on February 18, 2021, beginning its mission to search for signs of ancient life.",
            "expected": "REAL"
        },
        {
            "text": "The World Health Organization reports that COVID-19 vaccines have been proven safe and effective in clinical trials.",
            "expected": "REAL"
        },
        {
            "text": "Scientists discover new species of deep-sea creatures in the Pacific Ocean during research expedition.",
            "expected": "REAL"
        },
        {
            "text": "Global temperatures continue to rise, with 2023 being one of the warmest years on record according to climate data.",
            "expected": "REAL"
        },
        {
            "text": "Researchers develop new renewable energy technology that could reduce carbon emissions by 50%.",
            "expected": "REAL"
        }
    ]
    
    correct_predictions = 0
    total_tests = len(test_cases)
    
    print(f"Testing {total_tests} news articles...")
    print()
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Test {i}/{total_tests}:")
        if test_news_article(test_case["text"], test_case["expected"]):
            correct_predictions += 1
    
    # Calculate accuracy
    accuracy = (correct_predictions / total_tests) * 100
    
    print("📊 FINAL RESULTS:")
    print("=" * 60)
    print(f"✅ Correct Predictions: {correct_predictions}/{total_tests}")
    print(f"🎯 Accuracy: {accuracy:.1f}%")
    
    if accuracy >= 80:
        print("🌟 EXCELLENT - System is working very well!")
    elif accuracy >= 70:
        print("👍 GOOD - System is working well!")
    elif accuracy >= 60:
        print("⚠️ FAIR - System needs improvement")
    else:
        print("❌ POOR - System needs significant improvement")
    
    print()
    print("💡 The system should correctly identify:")
    print("   • Fake news with sensational language and conspiracy theories")
    print("   • Real news with factual, well-sourced information")
    print("   • The accuracy should be above 80% for a good system")

if __name__ == "__main__":
    main()
