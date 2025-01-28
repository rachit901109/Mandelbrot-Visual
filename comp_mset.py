import matplotlib.pyplot as plt
import numpy as np

r = -2
img = -1.5
x=[]
y=[]

for i in range(9):
    if i==0:
        newr = r
        newi = img
    else:
        newr, newi = ((newr**2 - newi**2)) + r, ((2*newr*newi) + img)
#    print(f"r = {r} img = {img} newr = {newr} newi = {newi}")
    print(f"Z{i} = {newr} + {newi}j")
    x.append(newr)
    y.append(newi)
    

#plt.scatter(x,y)
#plt.show()
