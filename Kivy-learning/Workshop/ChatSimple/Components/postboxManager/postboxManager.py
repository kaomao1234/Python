class PostboxManager:
    def __init__(self,text:str,comment=[]):
        self.heart:str = None
        self.text:str = str(text)
        self.comment:list[str] = comment
        self.score:int = 0
        self.heart_plus_iconlst = ['heart-plus-outline','heart-plus']
        self.heart_remove_iconlst = ['heart-remove-outline','heart-remove']
        self.heart_plus = self.heart_plus_iconlst[0]
        self.heart_remove = self.heart_remove_iconlst[0]