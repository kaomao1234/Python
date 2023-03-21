import spoonacular as sp


class RecipeApi(sp.API):
    key = "0d4a0a0bb378420b914c17b320536fa0"

    def __init__(self):
        super().__init__(api_key=self.key)
