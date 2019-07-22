import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#matplotlib inline
#select the style of the plot
style.use('ggplot')

x = np.linspace(0,5,11)
y = x**2

figure = plt.figure()
axes1=figure.add_axes([0.1,0.1,.8,.8])
axes2=figure.add_axes([0.2,0.5,.4,.3])
plt.show()

figure = plt.figure()
axes1=figure.add_axes([0.1,0.1,.8,.8])
axes2=figure.add_axes([0.6,0.15,.4,.3])
plt.show()


figure = plt.figure()
axes1=figure.add_axes([0.1,0.1,.8,.8])
axes2=figure.add_axes([0.2,0.5,.4,.3])
axes1.plot(x,y)
axes2.plot(y,x,'b')
axes1.set_title('Larger plot')
axes2.set_title('smaller plot')

plt.show()




