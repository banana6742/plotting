import matplotlib.pyplot as plt

# if i want to use matplotlib in the vsc
# comment the %matplotlib line

# %matplotlib inline

import numpy as np
x = np.linspace(0,5,11)
y = x**2

#Use similar to plt.figure() except use tuple unpack to grab fig and axes
fig, axes = plt.subplots()

#now use the axes object to add stuff to plot
axes.plot(x,y,'r')
axes.set_xlable('x')
axes.set_ylable('y')
axes.set_title('title')

#Empty canvas of 1 by 2 subplots
fig,axes = plt.subplots(nrows=1,ncols=2)

fig,axes = plt.subplots(nrows=3,ncols=2)

fig,axes=plt.subplots(nrows=3,ncols=3)

fig,axes=plt.subplots(nrows=3,ncols=3)
plt.tight_layout()

fig,axes=plt.subplots(ncols=2,nrows=1)
for currenct_ax in axes:
    current_ax.plot(x,y)

axes

fig,axes=plt.subplots(ncols=2,nrows=1)
axes[0].plot(x,y)

fig,axes=plt.subplots(ncols=2,nrows=1)
axes[1].plot(y,x)

fig,axes=plt.subplots(ncols=2,nrows=1)
axes[0].plot(x,y)
axes[0].set_title('First')

axes[1].plot(y,x)
axes[1].set_title('Second')

fig.savefig('1.png')


# import os
# os.chdir("C:\\Users\\banan\\Desktop\\python\\machinelearning\\CSV")

# #i cn also put the dpi
# fig.savefig('1.png',dpi=2000)

# #adding the legend
# fig=plt.figure()
# ax=fig.add_axes([0,0,1,1])
# ax.plot(x,x**2,label='X-axis')
# ax.plot(x,x**3,label='Y-axis')
# ax.legend()






# def f(t):
#     return np.exp(-t)*np.cos(2*np.pi*t)

# t1 = np.arange(0,5,0.1)
# t2 = np.arange(0,5,0.02)

# plt.figure(1)
# plt.subplot(211)
# plt.plot(t1,f(t1),'bo',t2,f(t2),'k')

# plt.subplot(212)
# plt.plot(t2,np.cos(2*np.pi*t2),'r--')
# plt.show()
