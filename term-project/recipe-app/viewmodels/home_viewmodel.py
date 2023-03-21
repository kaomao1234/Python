from app.api import RecipeApi


class HomeViewModel:
    def __init__(self):
        self.api = RecipeApi()

    def get_random_recipes(self) -> list[str]:
        titles = []
        for i in self.api.get_random_recipes(number=50).json()['recipes']:
            titles.append({"text": i['title']})
        return titles
