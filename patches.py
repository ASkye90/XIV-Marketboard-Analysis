import pandas as pd

PATCH_LIST_URL = "https://raw.githubusercontent.com/xivapi/ffxiv-datamining-patches/master/patchlist.json"
patch_list_df = pd.read_json(PATCH_LIST_URL)
patch_list_df.set_index("ID",inplace=True)

class Patch:
    def __init__(self,_id):
        self._id = _id
        self._patch = patch_list_df.loc[self._id]

    @property
    def version(self):
        return self._patch["Version"]

    @property
    def release_date(self):
        return patch_list_df["ReleaseDate"].get(self._id)

    @property
    def name(self):
        return patch_list_df