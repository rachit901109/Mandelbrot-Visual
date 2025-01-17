import matplotlib.pyplot as plt
import numpy as np

N=10
nums = np.linspace(-1, 1, 9).tolist()
all_x = []
all_y = []

print("Index ",end="")
for i in nums:
    print(str(i), end=" ")
print("\n") 

def get_ycords(x):
    a = 0
    vals=[]
    for i in range(N):
        try:
            b = (a**2)+x
            a = b
            vals.append(b)
        except OverflowError as e:
            print("got overflow for x={x}")
            return []
    return vals

#for x in nums:
#    xcord = [x for i in range(N)]
#    ycord = get_ycords(x)
#    #print(f"For x={x} y={ycord}\n")
#    if len(ycord)>0:
#        all_x.extend(xcord)
#        all_y.extend(ycord)

#plt.scatter(all_x,all_y,)
#plt.show()

for i in range(N):
    print("0.0 ", end="")
print("\n")

for x in nums:
    y = get_ycords(x)
    if len(y)>0:
        all_y.append(y)

for i in range(N):
    print(i+1, end=" ")
    ele = [r[i] for r in all_y]
    for x in ele:
        print(f"{x:.3e}", end=" ")
    print("\n")
