import seaborn as sns
# %matplotlib inline    

#data 
#Data 
#Seaborn comes withd built-in data sete!
#distplot--univarent only one type of data
tips = sns.load_dataset('tips')
tips.head()

sns.distplot(tips['total_bill'])    

#to remove the kde layer and just have the histogram use:
sns.distplot(tips['total_bill'],kde=False,bins=30)

#jointplot
sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')
sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde') 
sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg') 
sns.jointplot(x='total_bill',y='tip',data=tips,kind='resid')
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex') 
