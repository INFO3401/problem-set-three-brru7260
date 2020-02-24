# from utils import *
# import pandas as pd

import pandas as pd
def loadAndCleanData():
    item = pd.read_csv("creditData.csv")
    data = item.fillna(0)
    print(data)
loadAndCleanData()

# def computerProbability(feature,bin,data):
# 	count = 0.0
# # count the number of datapoints in the bin
# 	for datapoint in data.iterrows():
# # see if the data is in the right bin
# 		if datapoint[feature] >= bin[0] and datapoint[feature] < bin[1]:

# 			count += 1

# 			return (probability)
# # count the total number of datapoints
# totalData = len(data)
# # divide the number of people in the bin by the total numner of people
# probability = count / totalData
# # return the result

