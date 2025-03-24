import pandas as pd
import patches

RECIPE_URL = "https://raw.githubusercontent.com/xivapi/ffxiv-datamining/master/csv/Recipe.csv"
recipes_df = pd.read_csv(RECIPE_URL, skiprows=[0, 2])
recipes_df.set_index("#", inplace=True)

RECIPE_PATCH_URL = "https://raw.githubusercontent.com/xivapi/ffxiv-datamining-patches/master/patchdata/Recipe.json"
recipe_patch_df = pd.read_json(RECIPE_PATCH_URL, orient='index')
recipe_patch_df.columns = [0]


class Recipe:
    def __init__(self, index):
        self._index = index

    @property
    def index(self):
        return self._index

    @property
    def patch_number(self):
        return patches.get_version_by_patch_id(recipe_patch_df[0].get(self._index))
