import numpy as np
import matplotlib.pyplot as plt

tid = [0,1,2,5,7,10,15,20,25,30,35,40,45,50,60,70,80,90,100,120]
temp = [70.5,69.0,67.8,63.8,61.8,58.2,53.4,49.8,46.6,43.8,41.0,39.0,37.2,35.6,33.3,31.2,29.5,28.0,26.8,25.7]

def T(a,t):
    return 47.5 * np.e ** (-a*t) + 23

a1 = 0.03
a2 = 0.027
a3 = 0.025

t = np.linspace(0, 120,100)

plt.plot(tid,temp,label = 'Målte verdier')
plt.plot(t,T(a1,t),label = 'Newtons avkjølingslov(a=0.03)')
plt.plot(t,T(a2,t),label = 'Newtons avkjølingslov(a=0.027)')
plt.plot(t,T(a3,t),label = 'Newtons avkjølingslov(a=0.025)')

plt.title('Newtons avkjølingslov VS. målte verdier')
plt.grid('on')
plt.axhline(color='k')
plt.axvline(color='k')
plt.xlabel('Tid(min)')
plt.ylabel('Temperatur(C)')
plt.legend()
plt.show()
