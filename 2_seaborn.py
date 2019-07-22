import matplotlib.pyplot as plt
import seaborn as sns

tips=sns.load_dataset('tips')
print(tips.head())
# sns.distplot(tips['total_bill'])
# to remove KDE distribution from the graph
sns.distplot(tips['total_bill'],kde=False,color='r')

## pairplot 
## pairplot  will plot pairwise relationships across an entire dataframe (for the numerical columns) and supports a color hue arangement(for categorical columns).

## to plot pairwise realtionships across an entire data frame at least for the numerialc colmnns.

sns.pairplot(tips)
#graph for all numerical value

#now im selecting the columns if column have the same category like male, female
# i can apply hue to only category
# for for sex columns like male, female
sns.pairplot(tips,hue='sex')

#color with some specific color
sns.pairplot(tips,hue='sex',palette='coolwarm')

# rugplot

# rugplots are actually a very simple concept, they just draw a dash mark for every point on a univariate distribution.
# They are the building block of a KDE plot:

sns.rugplot(tips['total_bill'])

sns.distplot(tips['total_bill'],kde=False)

import seaborn as sns
sns.set(style='ticks')

df = sns.load_dataset("iris")
sns.pairplot(df,hue="species")


# # KDE plot
# kdeplots are Kernel Density Estimation plots.
# These KDE plots replace every single observation with Normal distribution centered around that value.For example

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

dataset = np.random.randn(25)

sns.rugplot(dataset);

#Set up the x-axis for the plot
x_min = dataset.min() - 2
x_max = dataset.max() + 2


#100 equally spaced points from x_min to x_max
x_axis = np.linspace(x_min, x_max,100)

#set up the bandwidth,for info on this:
url = 'https://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth'

bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**.2

#Create an empty kernel list
kernel_list = []

#plot each basis function
for data_point in dataset:
    
    #Create a kernel for each point and append to list
    kernel = stats.norm(data_point,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    
    #Scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis,kernel,color='grey',alpha=0.5)

plt.ylim(0,1)

#plot the sum of basis function
sum_of_kde = np.sum(kernel_list,axis=0)

#plot figure
fig = plt.plot(x_axis,sum_of_kde,color='indianred')

#Add the initila rugplot
sns.rugplot(dataset,c = 'indianred')

#Get rid of y-tick marks
plt.yticks([])

#set title
plt.suptitle("Sum of the Basis Functions")

sns.kdeplot(tips['total_bill'])
sns.rugplot(tips['total_bill'])

sns.kdeplot(tips['tip'])
sns.rugplot(tips['tip'])

# catgorical data plots
now let's discuss using seaborn to plot categorical data!
These are a few main plot types for this
* fatorplot
* boxplot
* violinplot
* stripplot
* swarmplot
* barplot
* countplot
Let's go through examples of each!

tips = sns.load_dataset('tips')
# tips
tips.head()

# barplot and countplot
These very similar plots allow you to get aggregate data off a categorical feature in your data.
barplot is a general plot tha allows you to aggregate the categorical data based off some functions, by default the mean.

sns.barplot(x='sex',y='total_bill',data=tips)

sns.barplot(x='sex',y='total_bill',data=tips, estimator=np.std)

# countplot
this is essentially the same as barplot except the explicily counting the number of occurences.
which is wyhy we only pass the x value.

# the same as a bar plot except the estimator is explicitly counting the number of occurences
sns.countplot(x='sex',data=tips)

# boxplot and violinplot
boxplots and violinplots are used to shown the distribution of categorical data. A box plot (or box-and-whisker plot) shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be “outliers” using a method that is a function of the inter-quartile range.

sns.boxplot(x="day",y="total_bill",data=tips)

#extra
#boxplot
sns.boxplot(x='sex',y='total_bill',data=tips)

## boxplot and violinplot

# boxplots and violinplots are used to shown the distribution of categorical data. A box plot (or box-and-whisker plot) shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be “outliers” using a method that is a function of the inter-quartile range.

sns.boxplot(x="day",y="total_bill",data=tips, palette='rainbow')

#Can do entire dataframe with orient='h'
sns.boxplot(data=tips,palette='rainbow',orient='h')

sns.boxplot(x="day",y="total_bill",hue="smoker",data=tips,palette="coolwarm")

violinplot
A violin plot plays a similar role as a box and whisker plot. 


It shows the distribution of quantitative data across several levels of one (or more) categorical variables such that those distributions can be compared. 


Unlike a box plot, in which all of the plot components correspond to actual datapoints, the violin plot features a kernel density estimation of the underlying distribution.

sns.violinplot(x="day",y="total_bill",data=tips,palette='rainbow')

sns.violinplot(x="day",y="total_bill",data=tips,hue='sex',palette='Set1')

sns.violinplot(x="day",y="total_bill",data=tips,hue="sex",split=True,palette='Set1')    

# stripplot and swarmplot
The stripplot will draw a scatterplot where one variable is categorical. A strip plot can be drawn on its own, but it is also a good complement to a box or violin plot in cases where you want to show all observations along with some representation of the underlying distribution.

The swarmplot is similar to stripplot(), but the points are adjusted (only along the categorical axis) so that they don’t overlap. This gives a better representation of the distribution of values, although it does not scale as well to large numbers of observations (both in terms of the ability to show all the points and in terms of the computation needed to arrange them).

sns.stripplot(x="day",y="total_bill",data=tips)
# sns.stripplot(x="day",y="total_bill",data=tips,jitter=False)

sns.stripplot(x="day",y="total_bill",data=tips,jitter=True)

sns.stripplot(x="day",y="total_bill",data=tips,jitter=True,hue='sex',palette='Set1')

sns.stripplot(x="day",y="total_bill",data=tips,jitter=True,hue='sex',palette='Set1',split=True)

sns.swarmplot(x="day",y="total_bill",data=tips)

sns.swarmplot(x="day",y="total_bill",hue='sex',data=tips,palette="Set1",split=True)

sns.violinplot(x="tip",y="day",data=tips,palette='rainbow')
sns.swarmplot(x="tip",y="day",data=tips,color='black',size=3)

# factorplot
factorplot is the most general form of a categorical plot.
It can take in a **kind** parameter to adjust the plot type:    

sns.factorplot(x='sex',y='total_bill',data=tips,kind='bar')