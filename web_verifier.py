#!/usr/bin/env python3
from typing import List, Dict, Tuple
from urllib.parse import urlparse
import re

from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup

TRUSTED_DOMAINS = {
    'reuters.com', 'apnews.com', 'bbc.com', 'bbc.co.uk', 'nytimes.com', 'washingtonpost.com',
    'theguardian.com', 'npr.org', 'associatedpress.com', 'factcheck.org', 'snopes.com', 'politifact.com',
    'fullfact.org', 'afp.com', 'apnews.com', 'bloomberg.com', 'wsj.com', 'aljazeera.com', 'cbsnews.com',
    'abcnews.go.com', 'nbcnews.com', 'sciencemag.org', 'nature.com', 'who.int', 'cdc.gov', 'europa.eu'
}

SUSPECT_DOMAINS = {
    'beforeitsnews.com', 'worldtruth.tv', 'yournewswire.com', 'infowars.com', 'naturalnews.com'
}

class WebVerifier:
    def __init__(self, max_results: int = 8, fetch_timeout: int = 6):
        self.max_results = max_results
        self.fetch_timeout = fetch_timeout

    def _extract_domain(self, url: str) -> str:
        try:
            netloc = urlparse(url).netloc.lower()
            # keep last two parts for domain.com, handle co.uk etc.
            parts = netloc.split('.')
            if len(parts) >= 2:
                return '.'.join(parts[-2:])
            return netloc
        except Exception:
            return ''

    def _credibility_label(self, domain: str) -> str:
        if domain in TRUSTED_DOMAINS:
            return 'trusted'
        if domain in SUSPECT_DOMAINS:
            return 'suspect'
        return 'unknown'

    def _score_overall(self, items: List[Dict]) -> Dict:
        trusted = sum(1 for i in items if i['credibility'] == 'trusted')
        suspect = sum(1 for i in items if i['credibility'] == 'suspect')
        total = max(1, len(items))
        support_score = sum(1 for i in items if i.get('stance') == 'supports')
        refute_score = sum(1 for i in items if i.get('stance') == 'refutes')
        neutral = total - support_score - refute_score

        # credibility score based on trusted vs suspect ratio
        credibility = max(0, min(100, int(60 + (trusted - suspect) * 10)))

        # verdict
        if refute_score > support_score and trusted > 0:
            verdict = 'LIKELY_FAKE'
        elif support_score > refute_score and trusted > 0:
            verdict = 'LIKELY_REAL'
        else:
            verdict = 'INCONCLUSIVE'

        return {
            'credibility_score': credibility,
            'verdict': verdict,
            'counts': {
                'trusted': trusted,
                'suspect': suspect,
                'neutral': neutral,
                'support': support_score,
                'refute': refute_score
            }
        }

    def _infer_stance_from_snippet(self, snippet: str) -> str:
        text = snippet.lower()
        refute_keywords = ['false', 'fake', 'hoax', 'debunk', 'not true', 'misleading', 'no evidence']
        support_keywords = ['confirms', 'confirmed', 'announced', 'reports', 'evidence shows', 'official']
        if any(k in text for k in refute_keywords):
            return 'refutes'
        if any(k in text for k in support_keywords):
            return 'supports'
        return 'neutral'

    def _safe_fetch_title(self, url: str) -> str:
        try:
            r = requests.get(url, timeout=self.fetch_timeout, headers={'User-Agent': 'Mozilla/5.0'})
            if r.ok and 'text/html' in r.headers.get('Content-Type', ''):
                soup = BeautifulSoup(r.text, 'html.parser')
                title = soup.title.string.strip() if soup.title and soup.title.string else ''
                return title[:200]
        except Exception:
            pass
        return ''

    def verify(self, text: str) -> Dict:
        query = text.strip()
        if len(query) > 220:
            query = query[:220]
        results: List[Dict] = []
        try:
            with DDGS() as ddgs:
                for res in ddgs.text(query, max_results=self.max_results, safesearch='moderate', timelimit='y'):  # past year
                    url = res.get('href') or res.get('url') or ''
                    title = res.get('title') or ''
                    snippet = res.get('body') or res.get('snippet') or ''
                    domain = self._extract_domain(url)
                    credibility = self._credibility_label(domain)
                    stance = self._infer_stance_from_snippet(snippet or title)
                    if not title:
                        title = self._safe_fetch_title(url)
                    results.append({
                        'title': title[:160] if title else '(No title)',
                        'snippet': snippet[:240] if snippet else '',
                        'url': url,
                        'domain': domain,
                        'credibility': credibility,
                        'stance': stance
                    })
        except Exception as e:
            return {'error': f'Web verification failed: {e}'}

        summary = self._score_overall(results)
        return {
            'query': query,
            'summary': summary,
            'sources': results
        }
