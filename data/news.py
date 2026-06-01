import requests
from bs4 import BeautifulSoup
from datetime import datetime

NEWS_FEEDS = [
    ("Economic Times", "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms"),
    ("Moneycontrol",   "https://www.moneycontrol.com/rss/business.xml"),
    ("LiveMint",       "https://www.livemint.com/rss/markets"),
]

POSITIVE = {"rally","surge","gain","rise","bullish","growth","profit","beat","strong","upgrade","buy","record"}
NEGATIVE = {"fall","drop","decline","crash","bearish","loss","miss","weak","downgrade","sell","slump","outflow"}


def fetch_news(max_per_feed: int = 5) -> list[dict]:
    headlines, headers = [], {"User-Agent": "Mozilla/5.0"}
    for source, url in NEWS_FEEDS:
        try:
            soup = BeautifulSoup(requests.get(url, headers=headers, timeout=8).content, "xml")
            for item in soup.find_all("item")[:max_per_feed]:
                title = item.find("title")
                headlines.append({"source": source, "title": title.text.strip() if title else "",
                                   "date": str(datetime.now().date())})
        except Exception:
            pass
    return headlines


def score_sentiment(headlines: list[dict]) -> float:
    if not headlines:
        return 0.0
    score = sum(
        sum(1 for w in h["title"].lower().split() if w in POSITIVE) -
        sum(1 for w in h["title"].lower().split() if w in NEGATIVE)
        for h in headlines
    )
    return max(-1.0, min(1.0, score / max(len(headlines), 1)))
