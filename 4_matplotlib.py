# use the jupyter
# simpli

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
#matplotlib inline

#generalte random numbers (total 10)
randomNumber=np.random.rand(10)
randomNumber

style.use('ggplot')
plt.plot(randomNumber,'g',label='line one',linewidth=2)
plt.xlabel('Range')
plt.ylabel('Numbers')
plt.title('First Plot')
plt.legend()
plt.show()
