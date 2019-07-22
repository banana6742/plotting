import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

t = np.arange(0,2,0.01)
s = 1 + np.sin(2*np.pi*t)

fig,ax = plt.subplots()
ax.plot(t,s)

ax.set(xlabel='time(s)',ylabel='voltage(mV)',
        title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()

plt.plot([1,2,3,4],[1,4,9,16],'ro')
# plt.plot([1,2,3,4],[1,4,9,16],'r')
plt.axis([0,6,0,20])
plt.show()

