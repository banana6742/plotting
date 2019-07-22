import matplotlib.pyplot as plt
fig = plt.figure()
x = [1,2,3,4]
y = [5,6,7,8]
ax  = fig.add_axes([0,0,1,1])
ax .plot(x,y)


fig = plt.figure()
x = [1,2,3,4]
y = [5,9,7,8]
ax = fig.add_axes([0,0,1,1])
# ax = plot(x,y,color="r")
ax.plot(x,y,color="#744323")  

ax.plot(x,y,color="#744323",linewidth=20)     

ax.plot(x,y,color="#744323",lw=20, alpha=.5)

ax.plot(x,y,color="#744323",lw=2, linestyle=':')
ax.plot(x,y,color="#744323",lw=2, ls='steps')

ax.plot(x,y,color="#744323",lw=2, ls=':',marker='o')
ax.plot(x,y,color="#744323",lw=2, ls=':',marker='+',markersize=20)

ax.plot(x,y,color="#468276",lw=10, ls='-',marker='o',markersize=26,markerfacecolor='red',markeredgewidth=2,markeredgecolor='black')


import numpy as np
x = np.linspace(0,5,11)
y = x**2
fig,ax = plt.subplots()

ax.plot(x,x+1,color='blue',alpha=0.5) #half-transparent
ax.plot(x,x+2,color="#8B0088")       #RGB hex code
ax.plot(x,x+3,color="#FF8C80")       #RGB hex code


fig,ax = plt.subplots(figsize=(12,6))
ax.plot(x,x+1,color="red",linewidth=0.25)
ax.plot(x,x+2,color="red",linewidth=0.5)
ax.plot(x,x+3,color="red",linewidth=1)
ax.plot(x,x+4,color="red",linewidth=2)

ax.plot(x,x+5,color="green",lw=3,linestyle='-')
ax.plot(x,x+6,color="green",lw=3,ls='-.')
ax.plot(x,x+7,color="green",lw=3,ls=':')

line, = ax.plot(x,x+8,color="black",lw=1.5)
line.set_dashes([5,10,15,10])

ax.plot(x,x+9,color="blue",lw=3,ls='-',marker='+')
ax.plot(x,x+10,color="blue",lw=3,ls='--',marker='o')
ax.plot(x,x+11,color="blue",lw=3,ls='-',marker='s') 
ax.plot(x,x+12,color="blue",lw=3,ls='--',marker='1')

ax.plot(x,x+13,color="purple",lw=1,ls='-',marker='o',markersize=2)
ax.plot(x,x+14,color="purple",lw=1,ls='-',marker='o',markersize=4)
ax.plot(x,x+15,color="purple",lw=1,ls='-',marker='o',markersize=8,markerfacecolor="red") 
ax.plot(x,x+16,color="purple",lw=1,ls='-',marker='s',markersize=8,markerfacecolor="yellow",markeredgewidth=3,markeredgecolor="green") 

fig =plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='purple',lw=2,ls='--')

x = np.linspace(0,2*np.pi,400)
y = np.sin(x**2)
fig,ax = plt.subplots()
ax.plot(x,y)
ax.set_title('A single plot')

fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x,y)
axs[1].plot(x,-y)

fig, (ax1,ax2) = plt.subplots(1,2)
fig.suptitle('Horizontally stacked subplots')
ax1.plot(x,y)
ax2.plot(x,-y)  

fig,axs = plt.subplots(2,2)
axs[0,0].plot(x,y)
axs[0,0].set_title('Axis[0,0]')
axs[0,1].plot(x,y,'tab:orange')
axs[0,1].set_title('Axis[0,1]')
axs[1,0].plot(x,-y, 'tab:green')
axs[1,0].set_title('Axis[1,0]')
axs[1,1].plot(x,-y,'tab:red')
axs[1,1].set_title('Axis[1,1]')

