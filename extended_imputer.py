import numpy as np
import pandas as pd

def ExtendedImputer(data, strategy):
    Extended = []
    for i in range(data.shape[0]):
        row = data.iloc[i]
        if np.isnan(row).any():
            Extended.append(1)
        else:
            Extended.append(0)
    if strategy=='mean':
        for i in range(data.shape[1]):
            column = data.iloc[:,i]
            column[column.isnull()]=np.nanmean(column)
    elif strategy=='median':
        for i in range(data.shape[1]):
            column = data.iloc[:,i]
            column[np.isnan(column)]=np.nanmedian(column)
    elif strategy=='most_frequent':
        for i in range(data.shape[1]):
            column = data.iloc[:,i]
            column[np.isnan(column)] = (column.value_counts()).index[0]
    else:
        for i in range(0,-1):
            column = data.iloc[:,i]
            column[np.isnan(column)]=strategy

    
    data['IsImputed']=Extended
    return data

data = pd.DataFrame(np.array([[1, 2, np.nan, 2],
                            [4, np.nan, 6, 4],
                            [7, 8, 9, np.nan],
                            [np.nan, 1, 4, 2],
                            [4, 2, 4, 4],
                            [8, 2, np.nan, 10]]))
# data = pd.read_csv("D:/test.csv")
print("Original Data: \n")
print(data,"\n")
print("Imputed Data")
print(ExtendedImputer(data, strategy='most_frequent'))
    

    
