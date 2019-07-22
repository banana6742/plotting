import matplotlib.pyplot as plt

# if i want to use matplotlib in the vsc
# comment the %matplotlib line

# %matplotlib inline

import numpy as np
x = np.linspace(0,5,11)
y = x**2

print(x)
print(y)
# functional method
print(plt.plot(x,y))
# print(plt.plot(x,y,'y-'))
#plt.show is keyword/function used to plot diagram
#in vsc
plt.xlabel('X side')
plt.ylabel('Y side')
plt.title('First Graph')
plt.show()

# plt.subplot(nrows,ncols,plot_number)
plt.subplot(1,2,1)
plt.plot(x,y,'r--')
plt.subplot(1,2,2)
plt.plot(y,x,'g--')
plt.show()

#create Figure(empty canvas)
fig =plt.figure()

#add set of axes to figure
axes = fig.add_axes([0.1,0.1,0.8,0.8]) #left,bottom,width,height(range 0 to 1)
#plot on that set of axes 
axes.plot(x,y,'b')
axes.set_xlabel('Set x Label')#notice the use of set_ to begin methods
axes.set_ylabel('Set y Label')
axes.set_title('Set Title')
plt.show()


