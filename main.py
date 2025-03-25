import datetime
import time
from patches import Patch
from datacenters import DataCenter
import items
import recipes
import sales
import worlds
from items import Item
from recipes import Recipe
import universalis

# for item in items.get_items_by_name("guile materia"):
# print(item.name)
# for item in items.get_all_items():
#     print(item.name)
# print(Item(35681).name)
# recipe = recipes.get_recipe_for(items.get_items_by_name("magitek")[0])
# if recipe:
#     print(recipe.patch.version)
#     print(recipe.result_item.name + ' ' + str(recipe.result_amount))
#     ingredients = recipe.ingredients
#     for item in ingredients.keys():
#         print(item.name + ' ' + str(ingredients[item]))
# print(Item(552).name)
# print(Recipe(30537).result_item.name)

# print(universalis.get_data_centers())
# print(universalis.get_available_worlds())
# print(universalis.get_market_sale_history(5,"Hyperion"))

# print(worlds.get_world("Hyperion").id)
# print(worlds.get_world(46).name)
#
now = time.time()
print(Item(5).name)
for sale in sales.get_sales([Item(5)],"Hyperion",int(now-20000000),int(now-10000000)):
    print(" ".join([sale.item.name,sale.buyer_name,str(sale.quantity),str(datetime.datetime.fromtimestamp(sale.timestamp))]))
