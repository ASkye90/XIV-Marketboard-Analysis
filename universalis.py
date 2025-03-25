import json
import time

import requests
from requests import Response

_calls = []
MAX_REQ = 20
MAX_PERIOD = 1


def _request_get(url: str, params: dict = None) -> Response:
    global _calls
    now = time.time()
    _calls = [call_time for call_time in _calls if call_time > now - MAX_PERIOD]
    if len(_calls) > MAX_REQ:
        time.sleep(MAX_PERIOD)
    now = time.time()
    _calls.append(now)
    response_ = requests.get(url, params=params)
    return response_


def get_data_centers() -> str:
    response_ = _request_get("https://universalis.app/api/v2/data-centers")
    return response_.text


def get_available_worlds() -> str:
    response_ = _request_get("https://universalis.app/api/v2/worlds")
    return response_.text


def get_market_current_data(item_ids: list[int], world_dc_region: str, listings: int = None, entries: int = None,
                            hq: bool = None, stats_within: int = None, entries_within: int = None,
                            fields: list[str] = None, user_agent: str = None) -> json:
    params = {
        "listings": listings,
        "entries": entries,
        "hq": hq,
        "statsWithin": stats_within,
        "entriesWithin": entries_within,
        "fields": ",".join(fields),
        "user_agent": user_agent
    }
    response_ = _request_get(f"https://universalis.app/api/v2/{world_dc_region}/{item_ids}", params)
    return response_.json()


def get_market_sale_history(item_ids: str, world_dc_region: str, entries: int = None, stats_within: int = None,
                            entries_within: int = None, entries_until: int = None, min_sale_price: int = None,
                            max_sale_price: int = None) -> json:
    params = {
        "entriesToReturn": entries,
        "statsWithin": stats_within,
        "entriesWithin": entries_within,
        "entriesUntil": entries_until,
        "minSalePrice": min_sale_price,
        "maxSalePrice": max_sale_price
    }
    response_ = _request_get(f"https://universalis.app/api/v2/history/{world_dc_region}/{item_ids}", params)
    return response_.json()
