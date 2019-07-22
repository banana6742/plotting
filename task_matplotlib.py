import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x = np.arange(0,9)
y = x**2

figure = plt.figure()
axes1=figure.add_axes([0.1,0.1,.8,.8])
axes2=figure.add_axes([0.6,0.1,.3,.3])
axes1.plot(x,y)
axes2.plot(x,y,'y')
axes1.set_title('Bigger')
axes2.set_title('Smaller')
plt.show()