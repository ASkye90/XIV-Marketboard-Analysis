import pandas as pd
from patches import Patch
from items import Item

RECIPE_URL = "https://raw.githubusercontent.com/xivapi/ffxiv-datamining/master/csv/Recipe.csv"
_recipes_df = pd.read_csv(RECIPE_URL, skiprows=[0, 2])
_recipes_df.set_index("#", inplace=True)

RECIPE_PATCH_URL = "https://raw.githubusercontent.com/xivapi/ffxiv-datamining-patches/master/patchdata/Recipe.json"
_recipe_patch_df = pd.read_json(RECIPE_PATCH_URL, orient='index')
_recipe_patch_df.columns = ["PatchId"]

MAX_INGREDIENTS = 8


class Recipe:
    def __init__(self, index):
        self._index = index
        self._recipe = _recipes_df.loc[index]

    @property
    def index(self):
        return self._index

    @property
    def patch(self):
        return Patch(_recipe_patch_df["PatchId"].get(self._index))

    @property
    def result_item(self):
        return Item(self._recipe["Item{Result}"])

    @property
    def result_amount(self):
        return self._recipe["Amount{Result}"]

    @property
    def ingredients(self):
        ingredients = {}
        for i in range(MAX_INGREDIENTS):
            id_ = self._recipe[f"Item{{Ingredient}}[{i}]"]
            amount = self._recipe[f"Amount{{Ingredient}}[{i}]"]
            # Unused ingredient values are set to 0
            if id_ > 0 and amount > 0:
                ingredients[Item(id_)] = amount
        return ingredients


_recipes_list = []
for _index, row in _recipes_df.iterrows():
    _recipes_list.append(Recipe(_index))


def get_all_recipes():
    return _recipes_list


def get_recipe_for(item):
    for recipe in _recipes_list:
        if recipe.result_item.index == item.index:
            return recipe
    return
