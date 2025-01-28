import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

N=5000
tol=2
x = np.linspace(-2, 0.75, N, dtype=np.float128)
y = np.linspace(-1.25, 1.25, N, dtype=np.float128)
#print(x, y, sep="\n")
xx, yy = np.meshgrid(x, y)

#print(xx, yy, xx.shape, sep="\n"+"--"*30+"\n")

for i in range(15):
    if i==0:
        newr = xx
        newi = yy
    else:
        newr, newi = ((np.power(newr, 2) - np.power(newi, 2))+xx), ((2*newr*newi)+yy)
#print("--"*30)
#print(newr, newi, newr.dtype, sep="\n"+"--"*30+"\n")
mod = np.sqrt(np.power(newr, 2) + np.power(newi, 2))
cm = np.where((mod-np.float128(tol))<=1e-6, True, False)
img = Image.fromarray(cm)
img.save('pil_image.png')
#plt.scatter(xx, yy, c=cm, s=2, cmap="Greys")
#plt.axis("off")
##plt.show()
#plt.savefig('test.png', dpi=512, bbox_inches='tight') 
