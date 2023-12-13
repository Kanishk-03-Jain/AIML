import pandas as pd
import numpy as np
def OneHotEncoder(data,column):
    # data.copy()
    unique_values=data[column].unique()
    for value in unique_values:
        new_column = f"{value}"
        data[new_column]=(data[column]==value).astype(int)
        # to get true false instead
        # data[new_column]=(data[column]==value)
    data = data.drop(column, axis=1)

    return data

data = pd.DataFrame({'Id':[1,2,3,4,5,6,7,8,9,10], 
                     'Rating':['Poor', 'Good', 'Fine', 'Poor', 'Poor', 'Fine', 'Good', 'Good', 'Good', 'Poor'],
                    'colors':['Red', 'Green', 'Blue', 'Red', 'Green', 'Blue', 'Red', 'Green', 'Blue', 'Green']})
print('Original Data:')
print(data,"\n")
print('OneHotEncoded Data: ')
print(OneHotEncoder(OneHotEncoder(data, 'colors'), 'Rating'))
