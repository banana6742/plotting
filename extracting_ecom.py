

import pandas as pd

import os
os.chdir('C:\\Users\\banan\\Desktop\\python\\machinelearning')


ecom = pd.read_csv('Ecommerce Purchases')

# Check the head of the DataFrame
print(ecom.head())

# How many rows and columns are there?
print(ecom.info())
print('-'*60)

#what is the average purchase price?
print(ecom['Purchase Price'].mean())
print('-'*60)

#all columns is the datasheet
a = ecom.columns
print(a)

#what is the average Purchase Price?


#What were the highest and lowest purchase prices?
print('-'*60)
print(ecom['Purchase Price'].max())
print('-'*60)
print(ecom['Purchase Price'].min())

# how many people have English 'en' as their language of choice on the website?
print(ecom[ecom['Language']=='en'])
print(ecom[ecom['Language']=='en'].count())
print('-'*75)
print(ecom[ecom['Language']=='en']['Language'].count())
print('-'*75)


print(ecom[ecom['Job']=='Lawyer'].info())
print('-'*75)
print(ecom[ecom['Job']=='Lawyer'].count())
print('-'*75)
print(ecom[ecom['Job']=='Lawyer']['Job'].count())
print('-'*75)
print(ecom[ecom['Job']=='Lawyer']['Job'].index)

#how many ppl made the purchase during the AM and how many ppl made the purchase during pM?
#Hint:Check out value_counts()
print(ecom['AM or PM'].value_counts())
print('-'*75)

#what are the 5 most common Job Titles?
print(ecom['Job'].value_counts().head())
print('-'*75)

#someone made a purchase that came from Lot:"90WT",what was the Purchase Price for this transaction?
print(ecom[ecom['Lot']=='90 WT']['Purchase Price'])
print('-'*75)

#what is the email of the person with the following credit card number:************
print(ecom[ecom['Credit Card']==4926535242672853]['Email'])
print('-'*75)

# how many ppl have Amex as their credit card provider *and* made a purchase above $95?
print(ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count())
print('-'*75)
print('-'*75)
# print(sum(ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count()))

print('-'*75)
#how many ppl have a credit card that expires in 2025?
print(sum(ecom['CC Exp Date'].apply(lambda x:x[3:])=='25'))
print('-'*75)

