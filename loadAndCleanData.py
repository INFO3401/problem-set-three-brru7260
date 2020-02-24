from utils import *

df = loadAndCleanData("creditdata.csv")

print("The probability is: ")
print(computeProbability("age", [0,40], df))


