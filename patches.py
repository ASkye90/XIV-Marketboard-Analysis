import pandas as pd

PATCH_LIST_URL = "https://raw.githubusercontent.com/xivapi/ffxiv-datamining-patches/master/patchlist.json"
patch_list_df = pd.read_json(PATCH_LIST_URL)
patch_list_df.set_index("ID",inplace=True)

def get_version_by_patch_id(id):
    return patch_list_df["Version"].get(id)
