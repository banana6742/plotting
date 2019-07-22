import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#evenly sampled time at 200ms intervals
t = np.arange(0.,5.,0.2)

#red dashes,blue squares and green triangles
plt.plot(t, t, 'r--',t, t**2,'bs',t, t**3,'g^')
plt.show()

names = ['group_a','group_b','group_c']
values = [1,10,100]

plt.figure(figsize=(9,3))
plt.subplot(131)
plt.bar(names,values)
plt.subplot(132)
plt.scatter(names,values)
plt.subplot(133)
plt.plot(names,values)
plt.suptitle('Categorical Plotting')
plt.show()

