import json

import pandas as pd
import universalis
from datetime import datetime
from worlds import World
from io import StringIO
from items import Item
from worlds import World


class Sale:
    def __init__(self, item_id, world_id, entry):
        self._item = Item(item_id)
        self._world = World(world_id)
        self._entry = entry

    @property
    def item(self) -> Item:
        return self._item

    @property
    def world(self) -> World:
        return self._world

    @property
    def hq(self) -> bool:
        return self._entry["hq"]

    @property
    def quantity(self) -> int:
        return self._entry["quantity"]

    @property
    def buyer_name(self) -> str:
        return self._entry["buyerName"]

    @property
    def timestamp(self) -> int:
        return self._entry["timestamp"]


def get_sales(items: list[Item], world_dc_region: str, from_date: int, to_date: int) -> list[Sale]:
    if to_date < from_date:
        raise ValueError("Invalid time frame from " + str(datetime.fromtimestamp(from_date)) + " to "
                         + str(datetime.fromtimestamp(to_date)))
    sales_list = []
    sales = universalis.get_market_sale_history(",".join([str(item.id) for item in items]), world_dc_region,
                                                entries_within=to_date - from_date, entries_until=to_date)
    if len(items) > 1:
        for item in sales["items"].values():
            for sale in item["entries"]:
                sales_list.append(Sale(item["itemID"], item["worldID"], sale))
    else:
        for sale in sales["entries"]:
            sales_list.append(Sale(sales["itemID"], sales["worldID"], sale))
    return sales_list
