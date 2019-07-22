#import numpy for generating random numbers
import numpy as np
#imprort matplotlib library
import matplotlib.pyplot as plt
from matplotlib import style
#vs上ではmatplotlibをコメントにする
# %matplotlib inline


# generate random numbers(total10)
randomNumber = np.random.rand(10)
#view them
randomNumber

# select the style of the plot
style.use('ggplot')
# plot the random number
plt.plot(randomNumber,'g',label='line one',linewidth=2)
# x axis is number of random numbers (index)
plt.xlabel('Range')
#y axis is actual random number
plt.ylabel('Numnbers')
#title of the plot
plt.title('First plot')

plt.legend()
plt.show()


