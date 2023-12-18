import pandas as pd
import numpy as np
import statistics
#In normalisation all values are in range 0 - 1
def Normalisation(data):
    scaled_data = data.copy()
    for column in data.columns:
        max = data[column].max()
        min = data[column].min()
        scaled_data[column] = (data[column]-min)/(max-min)
    return scaled_data

#In standarisation mean in 0 and std is 1
def Standardisation(data):
    scaled_data = data.copy()
    for column in data.columns:
        avg = data[column].mean()
        s=0
        # for i in data[column]:
        #     s += (i-avg)**2
        # std = (s/len(data[column]))**0.5
        std = np.std(data[column])
        # std = statistics.stdev(data[column])
        scaled_data[column] = (data[column]-avg)/std
    return scaled_data
data = pd.DataFrame({1:[1,2,3,4,5], 2:[6,7,8,9,10], 3:[11,12,13,14,15]})
print("Original Data: ")
print(data)
scale = "S"
if scale == "S":
    scaled_data = Standardisation(data)
elif scale == "N":
    scaled_data = Normalisation(data)
print("Scaled Data: ")
print(scaled_data)