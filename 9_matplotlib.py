import matplotlib.pyplot as plt
# plt.plot([1,2,3],[6,5,4])
# plt.show()

# x=[1,2,3]
# y=[10,20,30]
# plt.plot(x,y)
# plt.show()

# x=[1,2,3]
# y=[6,5,4]
# plt.plot(x,y)
# plt.xlabel('X -axis')
# plt.ylabel('y -axis')
# plt.title('This is Title\n new line')
# plt.show()

#legends
# x=[1,2,3]
# y=[5,7,3]
# x2=[2,4,6]
# y2=[12,24,26]

# plt.plot(x,y,label='First Line')
# plt.plot(x2,y2,label='Second Line')
# plt.xlabel('Plot Number')
# plt.ylabel('Important Graph\n New line')
# plt.legend()
# plt.show()

# x=[12,34,56,66,77]
# y=[20,30,40,50,60]

# x2=[1,2,3]
# y2=[10,20,30]

# plt.bar(x,y,label='new bar',color='r')
# plt.bar(x2,y2,label='bars two',color='g')
# plt.legend()
# plt.show()

##sep1
# population_ages=[20,12,32,43,55,45,76,89,90,89,130,123,25]

# ids=[x for x in range(len(population_ages))]
# plt.bar(ids, population_ages, label='Graph')

# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

## step2
## if i use histgram
# population_ages=[20,55,65,45,2,34,64,65,68,61,67,97,45,32,34,34,22,5]
# bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
# plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)
# # rwidth=0.8 グラフの太さを変える
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

# x=[1,2,3,4,5,6,7,8,9]
# y=[5,2,3,4,4,3,5,7,2]

#changing the shapes
#https://matplotlib.org/3.1.1/api/markers_api.html

# plt.scatter(x,y,label='skitcat',color='k',marker='*',s=120)
# plt.scatter(x,y,label='skitcat',color='k',marker='p',s=120)
# plt.scatter(x,y,label='skitcat',color='k',marker='s',s=120)
# plt.scatter(x,y,label='skitcat',color='k',marker='v',s=120)
# plt.scatter(x,y,label='skitcat',color='y',marker='x',s=120)
# plt.scatter(x,y,label='skitcat',color='b',marker='^',s=120)


# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

days=[1,2,3,4,5]
sleeping=[7,8,9,11,7]
eating=[2,3,4,5,6]
working=[2,7,3,2,6]
playing=[8,7,9,1,3]

# stackplot dont allow u to create lable in the background
# plt.stackplot(days,sleeping,eating,working,playing,colors=['m','k','b','y'])
#below code doesnt run bcz of tk.label
#plt.stackplot(days,sleeping,eating,working,playing,colors=['m','k','b','y'],label='not shown)
# plt.legend()
# plt.show()

##step2
# plt.plot([],[],label='sleeping',color='m')
# plt.plot([],[],label='working',color='k')
# plt.plot([],[],label='playing',color='y')
# plt.plot([],[],label='eating',color='b')

# plt.stackplot(days,sleeping,eating,working,playing,colors=['m','k','b','y'])
# plt.legend()
# plt.show()

slices=[7,2,2,13]
activities=['sleeping','eating','working','playing']
cols=['g','m','r','b']
# #1
# plt.pie(slices,labels=activities,colors=cols)
# #2 start this plot at 90 degree
# plt.pie(slices,labels=activities,colors=cols,startangle=90)
# #3 shadow
# plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True)
# #4 eating out of the plot
# plt.pie(slices,labels=activities,colors=cols,startangle=90,explode=(0.1,0,0,0))
#5 making PERCENT in the graph
# plt.pie(slices,labels=activities,colors=cols,startangle=90,explode=(0,0.1,0.1,0),autopct='%1.2f%%')
plt.pie(slices,labels=activities,colors=cols,startangle=90,explode=(0,0.1,0.1,0),autopct='%1.1f%%')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Activity a day')
plt.legend()
plt.show()
