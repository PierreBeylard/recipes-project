import pandas as pd
from recipebook.data import Data

class Recipe (Data):

    def __init__(self):
        super().__init__()

    def get_scored_recipes(self): 
        df_recipe_items_score=self.recipe_item.merge(self.ingredient, left_on='ingredient_id',right_on='Id')
        self.recipe['Score']= df_recipe_items_score[['recipe_id','Score']].groupby([ "recipe_id"]).mean().reset_index()['Score']
        return self.recipe



        
    