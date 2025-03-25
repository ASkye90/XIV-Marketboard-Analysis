import numpy
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
    def __init__(self, id_):
        self._id = id_
        self._recipe = _recipes_df.loc[id_]

    @property
    def id(self) -> int:
        return self._id

    @property
    def patch(self) -> Patch:
        return Patch(_recipe_patch_df["PatchId"].get(self._id))

    @property
    def result_item(self) -> Item:
        return Item(self._recipe["Item{Result}"])

    @property
    def result_amount(self) -> int:
        return int(self._recipe["Amount{Result}"])

    @property
    def ingredients(self) -> list[(Item, int)]:
        ingredients = []
        for i in range(MAX_INGREDIENTS):
            id_ = self._recipe[f"Item{{Ingredient}}[{i}]"]
            amount = int(self._recipe[f"Amount{{Ingredient}}[{i}]"])
            # Unused ingredient values are set to 0
            if id_ > 0 and amount > 0:
                ingredients.append((Item(id_), amount))
        return ingredients


_recipes_list = []
for _index, row in _recipes_df.iterrows():
    _recipes_list.append(Recipe(_index))


def get_all_recipes() -> list[Recipe]:
    return _recipes_list


def get_recipe_for(item) -> Recipe:
    for recipe in _recipes_list:
        if recipe.result_item.id == item.id:
            return recipe
    return
