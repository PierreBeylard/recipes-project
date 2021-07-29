import pandas as pd
from recipebook.data import Data

class Ingredient (Data): 
    
    def __init__(self):
        super().__init__()

    def get_with_popularities(self):
        df_ingredient_count= pd.DataFrame({'in_nb_recipes' : self.recipe_item.groupby([ "ingredient_id"] ).size()}).reset_index()
        ingredients=self.ingredient.merge(df_ingredient_count,how='inner',left_on='Id',right_on='ingredient_id',suffixes=('_left', '_right'))
        ingredients=ingredients.drop('ingredient_id',axis=1)
        ingredients['Popular']= [1 if i > 1 else 0 for i in ingredients.in_nb_recipes]
        return ingredients 