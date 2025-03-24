import pandas as pd
import patches

ITEM_URL = "https://raw.githubusercontent.com/xivapi/ffxiv-datamining/master/csv/Item.csv"
items_df = pd.read_csv(ITEM_URL, skiprows=[0, 2], index_col=0)

ITEM_PATCH_URL = "https://raw.githubusercontent.com/xivapi/ffxiv-datamining-patches/master/patchdata/Item.json"
item_patch_df = pd.read_json(ITEM_PATCH_URL, orient='index')
item_patch_df.columns = [0]

def get_item_by_name(name):
    return Item(items_df.index[items_df["Singular"] == name.lower()][0])


class Item:
    def __init__(self, index):
        self._index = index

    @property
    def index(self):
        return self._index

    @property
    def name(self):
        return items_df["Name"].get(self._index)

    @property
    def patch_number(self):
        return patches.get_version_by_patch_id(item_patch_df[0].get(self._index))
