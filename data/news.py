import requests
from bs4 import BeautifulSoup
from datetime import datetime

NEWS_FEEDS = [
    ("Economic Times Markets", "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms"),
    ("Moneycontrol", "https://www.moneycontrol.com/rss/business.xml"),
    ("LiveMint Markets", "https://www.livemint.com/rss/markets"),
]

POSITIVE_WORDS = {"rally", "surge", "gain", "rise", "bullish", "growth", "profit", "beat", "strong", "upgrade", "buy"}
NEGATIVE_WORDS = {"fall", "drop", "decline", "crash", "bearish", "loss", "miss", "weak", "downgrade", "sell", "slump"}


def fetch_news(max_per_feed: int = 5) -> list[dict]:
    headlines = []
    headers = {"User-Agent": "Mozilla/5.0"}
    for source, url in NEWS_FEEDS:
        try:
            resp = requests.get(url, headers=headers, timeout=8)
            soup = BeautifulSoup(resp.content, "xml")
            items = soup.find_all("item")[:max_per_feed]
            for item in items:
                title = item.find("title")
                pub_date = item.find("pubDate")
                headlines.append({
                    "source": source,
                    "title": title.text.strip() if title else "",
                    "date": pub_date.text.strip() if pub_date else str(datetime.now().date()),
                })
        except Exception:
            pass
    return headlines


def score_sentiment(headlines: list[dict]) -> float:
    """Returns sentiment score: +1.0 (very bullish) to -1.0 (very bearish)"""
    if not headlines:
        return 0.0
    score = 0
    for h in headlines:
        words = h["title"].lower().split()
        score += sum(1 for w in words if w in POSITIVE_WORDS)
        score -= sum(1 for w in words if w in NEGATIVE_WORDS)
    return max(-1.0, min(1.0, score / max(len(headlines), 1)))


def get_stock_news(symbol: str) -> list[dict]:
    """Fetch Yahoo Finance news for a specific stock."""
    import yfinance as yf
    ticker = yf.Ticker(symbol)
    news = []
    try:
        for item in ticker.news[:5]:
            content = item.get("content", {})
            title = content.get("title", "")
            if title:
                news.append({"source": "Yahoo Finance", "title": title, "date": str(datetime.now().date())})
    except Exception:
        pass
    return news
