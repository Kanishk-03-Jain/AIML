import pandas as pd
import numpy as numpy
#this function takes the mapping of the categorical columns
def OrdinalEncoder_manualMapping(data, mapping1, mapping2):
    # for i in range(data.shape[1]):
    #     column = data.iloc[:,i]
    data.copy()
    data['Rating']=data['Rating'].map(mapping1)
    data['colors']=data['colors'].map(mapping2)
    return data

#if we want to automize the mapping 
def OrdinalEncoder_AutoMapping(data):
    data.copy()
    unique_values1 = data['Rating'].unique()
    mapping1={value:index+1 for index, value in enumerate(unique_values1)}
    data['Rating']= data['Rating'].map(mapping1)
    unique_values2 = data['colors'].unique()
    mapping2={value:index+1 for index, value in enumerate(unique_values2)}
    data['colors']= data['colors'].map(mapping2)
    return data



mapping1= {'Very Good':5, 'Good':4, 'Fine':3, 'Poor':2, 'Very Poor':1}
mapping2= {'Red': 1,'Green':2, 'Blue':3}
data = pd.DataFrame({'Id':[1,2,3,4,5,6,7,8,9,10], 
                     'Rating':['Poor', 'Very Good', 'Fine', 'Very Poor', 'Poor', 'Fine', 'Very Good', 'Good', 'Very Good', 'Very Poor'],
                    'colors':['Red', 'Green', 'Blue', 'Red', 'Green', 'Blue', 'Red', 'Green', 'Blue', 'Green']})
print('Original Data:')
print(data,"\n")
print('Encoded Data(manual): ')
print(OrdinalEncoder_manualMapping(data, mapping1, mapping2))
print('Encoded Data(auto): ')
print(OrdinalEncoder_AutoMapping(data))




