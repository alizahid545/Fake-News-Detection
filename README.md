# Fake News Detection System

A comprehensive machine learning-based system that analyzes news articles to determine their authenticity. Built with Python Flask, scikit-learn, and modern web technologies.

## 🚀 Features

- **Advanced ML Model**: Uses TF-IDF vectorization and Random Forest classification
- **Feature Extraction**: Analyzes text length, sentiment, punctuation patterns, and more
- **Modern Web Interface**: Beautiful, responsive UI with real-time analysis
- **Confidence Scoring**: Provides probability scores for predictions
- **Example Dataset**: Includes sample fake and real news for testing
- **Real-time Analysis**: Instant results with detailed statistics

## 🛠️ Installation

### Quick Start (Recommended)

**Windows Users:**
```bash
# Double-click start.bat or run in Command Prompt:
start.bat
```

**Linux/Mac Users:**
```bash
# Make script executable (first time only):
chmod +x start.sh

# Run the system:
./start.sh
```

### Manual Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd fake-NEWS-detecton
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   # Option 1: Use the startup script (recommended)
   python run.py
   
   # Option 2: Run directly
   python app.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## 📊 How It Works

### Machine Learning Pipeline

1. **Text Preprocessing**:
   - Converts text to lowercase
   - Removes special characters and digits
   - Tokenizes and cleans the text

2. **Feature Extraction**:
   - **TF-IDF Vectorization**: Converts text to numerical features
   - **Text Statistics**: Word count, text length, average word length
   - **Sentiment Analysis**: Polarity and subjectivity scores
   - **Punctuation Analysis**: Exclamation marks, question marks
   - **URL Detection**: Counts URLs in text
   - **Case Analysis**: Uppercase character frequency

3. **Classification**:
   - **Random Forest Classifier**: Ensemble method for robust predictions
   - **Probability Scoring**: Provides confidence levels for predictions

### Sample Dataset

The system includes a curated dataset with examples of:
- **Fake News**: Sensational headlines, conspiracy theories, miracle cures
- **Real News**: Scientific discoveries, verified reports, factual information

## 🎯 Usage

### Web Interface

1. **Enter News Text**: Paste or type the news article you want to analyze
2. **Click "Analyze News"**: The system will process the text and provide results
3. **Review Results**: See the prediction (FAKE/REAL) with confidence scores
4. **Try Examples**: Use the "Load Example" button to test with sample articles

### Testing the System

Run the automated test suite to verify everything works:

```bash
# Test the system (make sure the server is running first)
python test_system.py
```

### Generating More Training Data

To improve the model with more examples:

```bash
# Generate additional training data
python data_generator.py
```

### API Endpoints

- `GET /`: Main web interface
- `POST /predict`: Analyze news text
  ```json
  {
    "text": "Your news article text here"
  }
  ```
- `POST /train`: Retrain the model
- `GET /health`: System health check

## 📈 Model Performance

The system achieves high accuracy through:
- **Feature Engineering**: Multiple text analysis techniques
- **Ensemble Learning**: Random Forest with 100 estimators
- **Balanced Dataset**: Equal representation of fake and real news
- **Cross-validation**: Robust training methodology

## 🔧 Customization

### Adding Custom Datasets

1. Create a CSV file with columns: `text`, `label`
2. Update the `train()` method in `app.py`:
   ```python
   detector.train(data_path='your_dataset.csv')
   ```

### Modifying Features

Edit the `extract_features()` method to add new analysis techniques:
- Named Entity Recognition
- Readability scores
- Source credibility analysis
- Temporal patterns

### Model Tuning

Adjust hyperparameters in the `FakeNewsDetector` class:
- TF-IDF max_features
- Random Forest parameters
- Feature selection methods

## 🛡️ Limitations

- **Training Data**: Performance depends on quality and quantity of training data
- **Language**: Currently optimized for English text
- **Context**: May not capture complex contextual nuances
- **Bias**: Reflects patterns in training data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with Flask, scikit-learn, and Bootstrap
- Uses NLTK for natural language processing
- TextBlob for sentiment analysis
- Sample data includes common fake news patterns

## 📞 Support

For questions or issues:
1. Check the documentation
2. Review existing issues
3. Create a new issue with detailed information

---

**Note**: This system is for educational and research purposes. Always verify news from multiple reliable sources before making important decisions. 