# import matplotlib.pyplot as plt
# import csv

# x = []
# y = []

# with open('example.txt','r')as csvfile:
#     plots=csv.reader(csvfile,delimiter=',')
#     for row in plots:
#         x.append(int(row[0]))
#         y.append(int(row[1]))

# plt.plot(x,y,label='Loaded from the file')

# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('This is Graph')
# plt.legend()
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
x,y=np.loadtxt('example.txt',delimiter=',',unpack=True)
    
plt.plot(x,y,label="Easy Way to Do")
plt.xlabel('x')
plt.ylabel('y')
plt.title('This is Graph')
plt.legend()
plt.show()