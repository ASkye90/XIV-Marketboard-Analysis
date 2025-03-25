import time

import requests

_calls = []
MAX_REQ = 20
MAX_PERIOD = 1


def _request(url, params=None):
    global _calls
    now = time.time()
    _calls = [call_time for call_time in _calls if call_time > now - MAX_PERIOD]
    if len(_calls) > MAX_REQ:
        time.sleep(1)
    now = time.time()
    _calls.append(now)
    response = requests.get(url, params=params)
    return response


def get_data_centers():
    response = _request("https://universalis.app/api/v2/data-centers")
    return response.text


def get_available_worlds():
    response = _request("https://universalis.app/api/v2/worlds")
    return response.text


def get_market_current_data(item_ids, world_dc_region, listings=None, entries=None, hq=None, stats_within=None,
                            entries_within=None, fields=None, user_agent=None):
    params = {
        "listings": listings,
        "entries": entries,
        "hq": hq,
        "statsWithin": stats_within,
        "entriesWithin": entries_within,
        "fields": fields,
        "user_agent": user_agent
    }
    response = _request(f"https://universalis.app/api/v2/{world_dc_region}/{item_ids}", params)
    return response.json()


def get_market_sale_history(item_ids, world_dc_region, entries=None, stats_within=None, entries_within=None,
                            entries_until=None, min_sale_price=None, max_sale_price=None):
    params = {
        "entriesToReturn": entries,
        "statsWithin": stats_within,
        "entriesWithin": entries_within,
        "entriesUntil": entries_until,
        "minSalePrice": min_sale_price,
        "maxSalePrice": max_sale_price
    }
    response = _request(f"https://universalis.app/api/v2/history/{world_dc_region}/{item_ids}", params)
    return response.json()
