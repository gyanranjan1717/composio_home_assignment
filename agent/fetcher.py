"""Documentation and Web Fetcher with Caching and Composio Integration."""

import os
import re
import time
import hashlib
import requests
from bs4 import BeautifulSoup
from typing import Optional, Dict, Tuple

CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", ".cache")
os.makedirs(CACHE_DIR, exist_ok=True)

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


class DocFetcher:
    """Fetches and caches developer documentation pages."""

    def __init__(self, cache_dir: str = CACHE_DIR, timeout: int = 15):
        self.cache_dir = cache_dir
        self.timeout = timeout
        os.makedirs(self.cache_dir, exist_ok=True)

    def _get_cache_path(self, url: str, app_id: int) -> str:
        url_hash = hashlib.md5(url.encode("utf-8")).hexdigest()[:10]
        safe_url = re.sub(r"[^a-zA-Z0-9_-]", "_", url)[:30]
        filename = f"{app_id}_{safe_url}_{url_hash}.txt"
        return os.path.join(self.cache_dir, filename)

    def fetch_url(self, url: str, app_id: int, force_refresh: bool = False) -> Tuple[Optional[str], Optional[str]]:
        """
        Fetches the text content of a URL.
        Returns: (cleaned_text, resolved_url)
        """
        cache_path = self._get_cache_path(url, app_id)
        if not force_refresh and os.path.exists(cache_path):
            with open(cache_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read(), url

        try:
            resp = requests.get(
                url,
                headers=DEFAULT_HEADERS,
                timeout=self.timeout,
                allow_redirects=True
            )
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                # Remove script, style, navigation noise
                for s in soup(["script", "style", "nav", "footer", "noscript", "svg"]):
                    s.decompose()
                
                text = soup.get_text(separator="\n", strip=True)
                # Keep top 15,000 characters to cover key auth and intro docs without bloat
                cleaned_text = "\n".join([line for line in text.splitlines() if line.strip()])[:15000]

                with open(cache_path, "w", encoding="utf-8", errors="ignore") as f:
                    f.write(cleaned_text)

                return cleaned_text, resp.url
            else:
                return f"HTTP Error {resp.status_code} while fetching {url}", url
        except Exception as e:
            return f"Fetch exception: {str(e)}", url

    def fetch_app_docs(self, app_id: int, app_name: str, hint_url: str) -> Dict[str, str]:
        """Fetches primary hint URL and any linked authentication/api docs."""
        results = {}
        primary_text, final_url = self.fetch_url(hint_url, app_id)
        if primary_text:
            results[final_url or hint_url] = primary_text
        return results
