from pydantic import BaseModel, HttpUrl
from typing import Tuple, Optional, Dict, Any, Literal

class ScrapeRequest(BaseModel):
    url: HttpUrl
    full_content: str = "no"  # yes/no
    method: Literal["aiohttp", "playwright"] = "aiohttp"  # Choose scraping method
    stealth: bool = False     # Enable stealth mode
    cache: bool = True
    parse: bool = True
    use_proxy: bool = True
    proxy: Optional[Tuple[str, str, str, str]] = None
    headers: Optional[Dict[str, str]] = None