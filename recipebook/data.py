import pandas as pd 

class Data () : 
    path='/home/pierre/simplon/POO/recipes-project/data/csv/'

    def __init__ (self, recipes='recipe', ingredients='ingredient',recipe_items='recipe_item'):
        self.recipe = pd.read_csv(f'{self.path}{recipes}s.csv', delimiter=',')
        self.ingredient = pd.read_csv(f'{self.path}{ingredients}s.csv', delimiter=';', usecols= [0, 1, 2])
        self.recipe_item = pd.read_csv(f'{self.path}{recipe_items}s.csv', delimiter=';', usecols= [0, 1, 2, 3, 4])
        self.dict_keys=[recipes,ingredients,recipe_items]
        self.table=[self.recipe,self.ingredient,self.recipe_item]


    def get_data(self):
        return {i : j for i , j in zip(self.dict_keys,self.table)}