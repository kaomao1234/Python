import pprint

from app.api import RecipeApi

api = RecipeApi()
result = api.search_recipes_complex("p").json()
pprint.pprint(result)
