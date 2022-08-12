
#swatooth wave

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import scipy.signal as s

def f(t):
    if(-np.pi<=t<0.0):
        result = (t+np.pi)/np.pi
    if(0.0<=t<=np.pi):
        result = (t-np.pi)/np.pi
    return result

ff=np.vectorize(f)
L=np.pi
n=50
t,h=np.linspace(-np.pi,np.pi,1000,retstep=True)
y2=s.sawtooth(t)
plt.plot(t,y2)
an=[]
bn=[]
#Determionation of the coefficient of an and bn

for i in range(n):
    an.append(quad(lambda t:ff(t)*np.cos((i*np.pi*t)/L),-np.pi,np.pi)[0]/L)
    bn.append(quad(lambda t:ff(t)*np.sin((i*np.pi*t)/L),-np.pi,np.pi)[0]/L)

print("an: ",an)
print("bn: ",bn)
s=0.0
for i in range(n):
    if(i==0):
        s=s+(an[i]/2)
    else:
        s=s+an[i]*np.cos((i*np.pi*t)/L) + bn[i]*np.sin((i*np.pi*t)/L)
    
plt.plot(t,s)
plt.grid(True)
plt.show()









                
                         
                         
