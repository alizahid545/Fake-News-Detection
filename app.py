from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import re
import os
from typing import Any, Dict

# Import AI analyzer
try:
    from ai_analyzer import AIAnalyzer, HybridAnalyzer
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False
    print("AI analyzer not available. Install openai package for enhanced accuracy.")

app = Flask(__name__)

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class FakeNewsDetector:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
        self.classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        self.is_trained = False
        
    def preprocess_text(self, text):
        """Clean and preprocess text data"""
        if pd.isna(text):
            return ""
        
        # Convert to lowercase
        text = str(text).lower()
        
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        return text
    
    def extract_features(self, text):
        """Extract additional features from text"""
        blob = TextBlob(text)
        
        features = {
            'text_length': len(text),
            'word_count': len(text.split()),
            'avg_word_length': np.mean([len(word) for word in text.split()]) if text.split() else 0,
            'sentiment_polarity': blob.sentiment.polarity,
            'sentiment_subjectivity': blob.sentiment.subjectivity,
            'exclamation_count': text.count('!'),
            'question_count': text.count('?'),
            'uppercase_count': sum(1 for c in text if c.isupper()),
            'url_count': len(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text))
        }
        
        return features
    
    def train(self, data_path=None):
        """Train the model with sample data or provided dataset"""
        if data_path and os.path.exists(data_path):
            # Load custom dataset
            df = pd.read_csv(data_path)
        else:
            # Create sample dataset for demonstration
            df = self.create_sample_dataset()
        
        # Preprocess text
        df['cleaned_text'] = df['text'].apply(self.preprocess_text)
        
        # Extract features
        feature_data = []
        for text in df['cleaned_text']:
            features = self.extract_features(text)
            feature_data.append(features)
        
        feature_df = pd.DataFrame(feature_data)
        
        # Combine text features with extracted features
        X_text = self.vectorizer.fit_transform(df['cleaned_text'])
        X_features = feature_df.values
        
        # Combine features
        X_combined = np.hstack([X_text.toarray(), X_features])
        y = df['label'].values
        
        # Train classifier
        self.classifier.fit(X_combined, y)
        self.is_trained = True
        
        return accuracy_score(y, self.classifier.predict(X_combined))
    
    def create_sample_dataset(self):
        """Create a sample dataset for demonstration"""
        sample_data = {
            'text': [
                # Fake news examples
                "BREAKING: Scientists discover that drinking hot water with lemon cures all diseases instantly! This miracle cure has been hidden by big pharma for years.",
                "ALIENS CONFIRMED: Government admits to covering up extraterrestrial contact for decades. Shocking new evidence reveals everything.",
                "5G CAUSES COVID: New study proves that 5G networks are responsible for the coronavirus pandemic. Experts say radiation is the real culprit.",
                "FLAT EARTH PROVEN: NASA finally admits the Earth is flat after pressure from social media. All space photos were CGI.",
                "TIME TRAVEL ACHIEVED: Scientists successfully send a cat back to 1920. The cat returned with a message from the past.",
                
                # Real news examples
                "NASA's Perseverance rover successfully landed on Mars, beginning its mission to search for signs of ancient life.",
                "The World Health Organization reports that COVID-19 vaccines have been proven safe and effective in clinical trials.",
                "Scientists discover new species of deep-sea creatures in the Pacific Ocean during research expedition.",
                "Global temperatures continue to rise, with 2023 being one of the warmest years on record according to climate data.",
                "Researchers develop new renewable energy technology that could reduce carbon emissions by 50%.",
                "Study shows that regular exercise can improve mental health and reduce symptoms of depression.",
                "New cancer treatment shows promising results in early clinical trials, offering hope for patients.",
                "International space station celebrates 20 years of continuous human presence in space.",
                "Renewable energy sources now provide over 30% of global electricity generation.",
                "Scientists develop biodegradable plastic alternative made from plant materials."
            ],
            'label': [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 1 for fake, 0 for real
        }
        return pd.DataFrame(sample_data)
    
    def predict(self, text):
        """Predict whether a news article is fake or real"""
        if not self.is_trained:
            return {"error": "Model not trained. Please train the model first."}
        
        # Preprocess text
        cleaned_text = self.preprocess_text(text)
        
        # Extract features
        features = self.extract_features(cleaned_text)
        
        # Vectorize text
        text_vector = self.vectorizer.transform([cleaned_text])
        
        # Combine features
        X_combined = np.hstack([text_vector.toarray(), np.array([list(features.values())])])
        
        # Make prediction
        prediction = self.classifier.predict(X_combined)[0]
        probability = self.classifier.predict_proba(X_combined)[0]
        
        return {
            "prediction": "FAKE" if prediction == 1 else "REAL",
            "confidence": float(max(probability)),
            "fake_probability": float(probability[1]),
            "real_probability": float(probability[0]),
            "features": features
        }

# Initialize the detector
detector = FakeNewsDetector()

# Initialize AI analyzer if available
ai_analyzer = None
hybrid_analyzer = None
if AI_AVAILABLE:
    try:
        ai_analyzer = AIAnalyzer()
        hybrid_analyzer = HybridAnalyzer(detector, ai_analyzer)
        print("✅ AI analyzer initialized successfully!")
    except Exception as e:
        print(f"⚠️ AI analyzer initialization failed: {e}")
        ai_analyzer = None
        hybrid_analyzer = None

# Web verifier import
try:
    from web_verifier import WebVerifier
    web_verifier = WebVerifier()
    print("✅ Web verifier initialized")
except Exception as _e:
    web_verifier = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_news():
    try:
        data = request.get_json()
        news_text = data.get('text', '')
        use_ai = data.get('use_ai', True)  # Default to using AI if available
        
        if not news_text.strip():
            return jsonify({"error": "Please provide news text"}), 400
        
        # Train model if not already trained
        if not detector.is_trained:
            detector.train()
        
        # Use hybrid analysis if AI is available and requested
        if use_ai and hybrid_analyzer:
            result = hybrid_analyzer.analyze_hybrid(news_text)
            result['analysis_type'] = 'hybrid'
            result['ai_available'] = True
        else:
            # Fallback to ML only
            result = detector.predict(news_text)
            result['analysis_type'] = 'ml_only'
            result['ai_available'] = False
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/train', methods=['POST'])
def train_model():
    try:
        # Train the model
        accuracy = detector.train()
        return jsonify({
            "message": "Model trained successfully",
            "accuracy": accuracy
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy", 
        "model_trained": detector.is_trained,
        "ai_available": ai_analyzer is not None,
        "hybrid_available": hybrid_analyzer is not None
    })

@app.route('/ai_status')
def ai_status():
    """Check AI analyzer status and capabilities"""
    if ai_analyzer:
        return jsonify({
            "ai_available": True,
            "model": ai_analyzer.model,
            "capabilities": [
                "fake news detection",
                "credibility scoring",
                "red flag identification",
                "fact-checking recommendations"
            ]
        })
    else:
        return jsonify({
            "ai_available": False,
            "message": "OpenAI API key not configured or package not installed"
        })

@app.route('/verify', methods=['POST'])
def verify_on_web():
    """Verify the news text against web sources using DuckDuckGo search."""
    try:
        data: Dict[str, Any] = request.get_json() or {}
        news_text: str = data.get('text', '').strip()
        if not news_text:
            return jsonify({'error': 'Please provide news text'}), 400
        if web_verifier is None:
            return jsonify({'error': 'Web verifier not available'}), 500
        result = web_verifier.verify(news_text)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 