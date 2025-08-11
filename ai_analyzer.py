#!/usr/bin/env python3
"""
AI-Powered News Analyzer using ChatGPT/OpenAI API
Provides high-accuracy fake news detection through AI analysis
"""

import openai
import os
import json
import time
from typing import Dict, List, Optional

class AIAnalyzer:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the AI analyzer with OpenAI API"""
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        self.model = "gpt-3.5-turbo"  # Can be upgraded to gpt-4 for better accuracy
        
    def analyze_news_with_ai(self, text: str) -> Dict:
        """
        Analyze news text using ChatGPT for fake news detection
        Returns detailed analysis with confidence scores
        """
        if not self.api_key:
            return {
                "error": "OpenAI API key not found. Please set OPENAI_API_KEY environment variable.",
                "available": False
            }
        
        try:
            # Create a comprehensive prompt for fake news analysis
            prompt = self._create_analysis_prompt(text)
            
            # Get AI analysis using the new OpenAI API
            from openai import OpenAI
            client = OpenAI(api_key=self.api_key)
            
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert fact-checker and fake news detector. Analyze the given news article and provide a detailed assessment of its credibility."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.1,  # Low temperature for consistent results
                max_tokens=500
            )
            
            # Parse the AI response
            ai_response = response.choices[0].message.content
            analysis = self._parse_ai_response(ai_response)
            
            return {
                "ai_analysis": analysis,
                "raw_response": ai_response,
                "available": True
            }
            
        except Exception as e:
            return {
                "error": f"AI analysis failed: {str(e)}",
                "available": False
            }
    
    def _create_analysis_prompt(self, text: str) -> str:
        """Create a comprehensive prompt for AI analysis"""
        return f"""
Please analyze the following news article for potential fake news indicators. Provide your assessment in the following JSON format:

{{
    "credibility_score": 0-100,
    "is_likely_fake": true/false,
    "confidence": 0-100,
    "red_flags": ["list", "of", "red", "flags"],
    "green_flags": ["list", "of", "positive", "indicators"],
    "reasoning": "detailed explanation",
    "recommendations": "what to check or verify"
}}

News Article:
{text[:2000]}  # Limit text length for API efficiency

Focus on:
1. Sensational language and emotional manipulation
2. Lack of credible sources or citations
3. Conspiracy theory patterns
4. Miracle cure claims
5. Authority figure manipulation
6. Urgency and fear tactics
7. Contradictions with established facts
8. Professional journalistic standards
9. Source credibility
10. Factual accuracy indicators

Respond only with the JSON analysis.
"""
    
    def _parse_ai_response(self, response: str) -> Dict:
        """Parse the AI response into structured data"""
        try:
            # Try to extract JSON from the response
            if '{' in response and '}' in response:
                start = response.find('{')
                end = response.rfind('}') + 1
                json_str = response[start:end]
                return json.loads(json_str)
            else:
                # Fallback parsing
                return self._fallback_parsing(response)
        except json.JSONDecodeError:
            return self._fallback_parsing(response)
    
    def _fallback_parsing(self, response: str) -> Dict:
        """Fallback parsing when JSON parsing fails"""
        # Extract key information from text response
        response_lower = response.lower()
        
        # Determine if likely fake
        fake_indicators = ['fake', 'false', 'misleading', 'unreliable', 'credible', 'reliable']
        is_likely_fake = any(indicator in response_lower for indicator in ['fake', 'false', 'misleading', 'unreliable'])
        
        # Estimate confidence based on response length and content
        confidence = min(80, len(response) // 2)
        
        return {
            "credibility_score": 30 if is_likely_fake else 70,
            "is_likely_fake": is_likely_fake,
            "confidence": confidence,
            "red_flags": ["Unable to parse detailed analysis"],
            "green_flags": ["AI analysis completed"],
            "reasoning": response,
            "recommendations": "Verify with multiple sources"
        }
    
    def get_fact_checking_sources(self, topic: str) -> List[str]:
        """Get recommended fact-checking sources for a topic"""
        sources = [
            "Snopes.com",
            "FactCheck.org",
            "PolitiFact.com",
            "Reuters Fact Check",
            "Associated Press Fact Check",
            "BBC Reality Check",
            "Full Fact (UK)",
            "Science Feedback",
            "Lead Stories",
            "NewsGuard"
        ]
        return sources[:5]  # Return top 5 sources
    
    def analyze_multiple_articles(self, articles: List[str]) -> List[Dict]:
        """Analyze multiple articles in batch"""
        results = []
        for i, article in enumerate(articles):
            print(f"Analyzing article {i+1}/{len(articles)}...")
            result = self.analyze_news_with_ai(article)
            results.append(result)
            time.sleep(1)  # Rate limiting
        return results

class HybridAnalyzer:
    """Combines ML model with AI analysis for maximum accuracy"""
    
    def __init__(self, ml_model, ai_analyzer: AIAnalyzer):
        self.ml_model = ml_model
        self.ai_analyzer = ai_analyzer
    
    def analyze_hybrid(self, text: str) -> Dict:
        """Combine ML and AI analysis for best results"""
        
        # Get ML prediction
        ml_result = self.ml_model.predict(text)
        
        # Get AI analysis
        ai_result = self.ai_analyzer.analyze_news_with_ai(text)
        
        # Combine results
        if ai_result.get("available", False) and "ai_analysis" in ai_result:
            ai_analysis = ai_result["ai_analysis"]
            
            # Weight the results (AI gets higher weight for accuracy)
            ml_weight = 0.3
            ai_weight = 0.7
            
            # Calculate hybrid score
            ml_score = ml_result.get("confidence", 0.5)
            ai_score = ai_analysis.get("credibility_score", 50) / 100
            
            hybrid_score = (ml_score * ml_weight) + (ai_score * ai_weight)
            
            # Determine final prediction
            is_fake = hybrid_score < 0.5
            
            return {
                "prediction": "FAKE" if is_fake else "REAL",
                "confidence": hybrid_score,
                "ml_prediction": ml_result,
                "ai_analysis": ai_analysis,
                "hybrid_score": hybrid_score,
                "recommendations": ai_analysis.get("recommendations", "Verify with multiple sources"),
                "red_flags": ai_analysis.get("red_flags", []),
                "green_flags": ai_analysis.get("green_flags", [])
            }
        else:
            # Fallback to ML only if AI is not available
            return {
                "prediction": ml_result.get("prediction", "UNKNOWN"),
                "confidence": ml_result.get("confidence", 0.5),
                "ml_prediction": ml_result,
                "ai_analysis": {"error": "AI analysis not available"},
                "hybrid_score": ml_result.get("confidence", 0.5),
                "recommendations": "Use ML prediction only",
                "red_flags": [],
                "green_flags": []
            }

# Example usage and testing
if __name__ == "__main__":
    # Test the AI analyzer
    analyzer = AIAnalyzer()
    
    test_articles = [
        "BREAKING: Scientists discover that drinking hot water with lemon cures all diseases instantly! This miracle cure has been hidden by big pharma for years.",
        "NASA's Perseverance rover successfully landed on Mars, beginning its mission to search for signs of ancient life."
    ]
    
    for article in test_articles:
        print(f"\nAnalyzing: {article[:100]}...")
        result = analyzer.analyze_news_with_ai(article)
        print(f"Result: {result}")
