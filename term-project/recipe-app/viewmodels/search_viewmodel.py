from app.api import RecipeApi
from threading import Thread

class SearchViewModel:

    def __init__(self):
        self.api = RecipeApi()

    def search(self, text: str):
        data = []
        if text != '':
            for i in self.api.autocomplete_recipe_search(text).json():
                data.append({"text": i['title']})
        return data

    
