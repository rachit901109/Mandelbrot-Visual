import matplotlib.pyplot as plt
import numpy as np

N=2000
num=2
x = np.linspace(-1*num, num, N, dtype=np.float128)
y = np.linspace(-1*num, num, N, dtype=np.float128)
#print(x, y, sep="\n")
xx, yy = np.meshgrid(x, y)
#def inset(x,y):
#    for i in range(2):
#        if i==0:
#            newr = x
#            newi = y
#        else:
#            newr, newi = ((newr**2 - newi**2)+x), ((2*newr*newi)+y)
#        if abs(newr)>=np.float128(5) or abs(newi)>=np.float128(5):
#            return False
#    return True
#
#res = []
#for i in x:
#    temp = []
#    for j in y:
#        temp.append(inset(i,j))
#    res.append(temp)

#print(xx, yy, xx.shape, sep="\n"+"--"*30+"\n")

for i in range(15):
    if i==0:
        newr = xx
        newi = yy
    else:
        newr, newi = ((newr**2 - newi**2)+xx), ((2*newr*newi)+yy)
#print("--"*30)
#print(newr, newi, newr.dtype, sep="\n"+"--"*30+"\n")
#cond_x = (np.abs(newr)-np.float128(num))
#cond_y = (np.abs(newi)-np.float128(num))
#print(cond_x, cond_y, cond_y.dtype, sep="\n"+"--"*30+"\n")
bool_x = np.where((np.abs(newr)-np.float128(num))<=1e-3, True, False)
bool_y = np.where((np.abs(newi)-np.float128(num))<=1e-3, True, False)
cm = bool_x & bool_y

#print(bool_x, bool_y, cm, bool_x.dtype, sep="\n"+"--"*30+"\n")
# plt.scatter(xx, yy, c=res, cmap='Greys')
#plt.show()
plt.scatter(xx, yy, c=cm, s=2, cmap="Greys")
#plt.show()
plt.savefig('test.png', dpi=300, bbox_inches='tight') 
#fig, ax = plt.subplots(1, 2)
#ax[0].scatter(xx, yy, c=res, cmap="Spectral")
#ax[0].set_title("Iterative Method")
#ax[1].scatter(xx, yy, c=cm, cmap="Spectral")
#ax[1].set_title("Vector Method")
#plt.show()
