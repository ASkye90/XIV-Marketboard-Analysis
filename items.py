import pandas as pd

from patches import Patch

ITEM_URL = "https://raw.githubusercontent.com/xivapi/ffxiv-datamining/master/csv/Item.csv"
_items_df = pd.read_csv(ITEM_URL, skiprows=[0, 2], index_col=0)

ITEM_PATCH_URL = "https://raw.githubusercontent.com/xivapi/ffxiv-datamining-patches/master/patchdata/Item.json"
_item_patch_df = pd.read_json(ITEM_PATCH_URL, orient='index')
_item_patch_df.columns = [0]


class Item:
    def __init__(self, id_):
        self._id = id_
        self._item = _items_df.loc[id_]

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._item["Name"]

    @property
    def patch(self) -> Patch:
        return Patch(_item_patch_df[0].get(self._id))

    @property
    def description(self) -> str:
        return self._item["Description"]


_items_list = []
for i, row in _items_df.iterrows():
    _items_list.append(Item(i))


def get_all_items() -> list[Item]:
    """
    Get a list of all items
    :return: List of all items
    """
    return _items_list


def get_items(name) -> list[Item]:
    """
    Get a list of items that contain a given name
    :param name: Partial name of item
    :return: List of items or empty list if none exist
    """
    items = []
    for item in _items_list:
        if str(item.name).lower().__contains__(name.lower()):
            items.append(Item(item.id))
    return items
