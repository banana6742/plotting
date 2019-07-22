# import matplot library
import matplotlib.pyplot as plt
from matplotlib import style
# %matplotlib inline

# website traffic data
# number of users/ visitors on the web site
web_customers=[123,650,950,1290,1630,1450,1034,1295,1295,465,205,80]
# time distribution(hourly)
time_hrs=[7,8,9,10,11,12,13,14,15,16,17,18]
# select the style of the plot
style.use('ggplot')


# set label for the plot
# plt.plot(time_hrs,web_customrers)
# 点線、太さ、色を変えてみた。コメントを変更
# plt.plot(time_hrs,web_customers,color='b',linestyle='--',linewidth=2.5)
plt.plot(time_hrs,web_customers,'r',label='web traffic',linewidth=1.5)
plt.axis([6.5,17.5,50,2000])

plt.title('web site traffic')
# set label for x axis
plt.xlabel('Hrs')
# set label for y axis
plt.ylabel('Number of Uses')

plt.show()