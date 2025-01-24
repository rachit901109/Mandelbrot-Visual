import matplotlib.pyplot as plt
import numpy as np

N=100
nums = np.linspace(-2, 0, 100).tolist()
all_x = []
all_y = []

def get_ycords(x):
    a = 0
    vals=[]
    for i in range(N):
        try:
            b = (a**2)+x
            a = b
            vals.append(b)
        except OverflowError as e:
            print(f"got overflow for x={x}")
            return []
    return vals

for x in nums:
    xcord = [x for i in range(N)]
    ycord = get_ycords(x)
    #print(f"For x={x} y={ycord}\n")
    if len(ycord)>0:
        all_x.extend(xcord)
        all_y.extend(ycord)

plt.scatter(all_x,all_y,)
plt.show()

