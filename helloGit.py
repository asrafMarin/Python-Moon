
import numpy as np 

arr=np.array([10, 40, 50, 210, 11, 90, 60])

flary=[]

for ele in arr:
	if ele > 50:
		flary.append(True)
	else: 
		flary.append(False)

farry=arr[flary]
print(farry) 