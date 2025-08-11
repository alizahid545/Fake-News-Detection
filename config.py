"""
Configuration file for Fake News Detection System
"""

# Model Configuration
MODEL_CONFIG = {
    'tfidf_max_features': 5000,
    'random_forest_n_estimators': 100,
    'random_forest_random_state': 42,
    'test_size': 0.2,
    'random_state': 42
}

# Feature Extraction Configuration
FEATURE_CONFIG = {
    'min_text_length': 10,
    'max_text_length': 10000,
    'sentiment_weight': 1.0,
    'punctuation_weight': 1.0,
    'case_weight': 1.0,
    'url_weight': 2.0
}

# Web Interface Configuration
WEB_CONFIG = {
    'host': '0.0.0.0',
    'port': 5000,
    'debug': True,
    'threaded': True
}

# Data Configuration
DATA_CONFIG = {
    'sample_dataset_size': 100,
    'fake_news_ratio': 0.5,
    'real_news_ratio': 0.5,
    'min_confidence_threshold': 0.6
}

# API Configuration
API_CONFIG = {
    'max_request_size': 16 * 1024 * 1024,  # 16MB
    'rate_limit': 100,  # requests per minute
    'timeout': 30  # seconds
}

# Logging Configuration
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': 'fake_news_detector.log'
}

# Security Configuration
SECURITY_CONFIG = {
    'enable_cors': True,
    'allowed_origins': ['*'],
    'enable_rate_limiting': False,
    'max_text_length': 10000
}
