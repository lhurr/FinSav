from functools import cache
import requests
from src import YAHOO_FIN_SEARCH_BASE, DEFAULT_USER_AGENT
from src.ticker import TickerInfo
import re, os
from diskcache import Cache


CACHE_DIR = ".cache"
os.makedirs(CACHE_DIR, exist_ok=True)
_disk_cache = Cache(CACHE_DIR) 

def extract_companies_from_text(text):
    pattern = r'\[.*?\]'
    companies = []
    for match in re.findall(pattern, text):
        try:
            extracted_list = eval(match)  
            if isinstance(extracted_list, list):
                companies.extend(extracted_list)
        except SyntaxError:
            pass  
    return list(set(companies))


@cache
def list_all_topics():
    methods = []
    for name in dir(TickerInfo):
        attr = getattr(TickerInfo, name)
        if callable(attr) and not name.startswith("__"):
            methods.append(name)

    methods = list(set(methods))
    methods.append("none_of_above")
    return methods


def extract_mentioned_topics(text, top=3):
    topics = list_all_topics()
    mentioned_topics = [topic for topic in topics if topic in text]
    return mentioned_topics[:top]


def get_ticker_from_name(name):
    if name in _disk_cache:
        return _disk_cache[name]

    params = {"q": name}
    response = requests.get(
        YAHOO_FIN_SEARCH_BASE,
        params=params,
        headers={
            'User-Agent': DEFAULT_USER_AGENT,
            "content-type": "application/json"
        }
    )
    data = response.json()  
    try:
        record = data['quotes'][0]
        result = {
            "symbol": record['symbol'],
            "short_name": record['shortname'],
            "long_name": record['longname'],
            'exchange': record['exchange'],
        }
        # Cache the result
        _disk_cache[name] = result
        return result
    except (KeyError, IndexError):
        return None
