import numpy as np 
import pandas as pd 

iris= pd.read_csv("iris.csv")
iris.to_csv("iris2.csv") #converting into data frame to CSV again, check for more


f=open("iris2.csv")
print(f.read())