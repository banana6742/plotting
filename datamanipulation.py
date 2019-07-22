# how to create the Series
# run in jupyter

import numpy as np
import pandas as pd

# syntax
# S=pd.Series(data,index = [index])
anyname=pd.Series(list('abcdef'))
print(anyname)
print('-'*75)
print('-'*75)

np_country=np.array(['lohit','susumu','hika','kota','naoya'])
s_country=pd.Series(np_country)
print(s_country)
print('-'*75)
print('-'*75)

cal=pd.Series([1,2,3,4,5],index=['lohit','mohit','loadja','shai','sjaa'])
cal2=pd.Series(['lohit','mohit','loadja','shai','sjaa'],index=[1,2,3,4,5])
print(cal)
print('-'*75)
print(cal2)
print('-'*75)
print('-'*75)
print(cal[3])
print('-'*75)

print('slice=>\n',cal[1:4])
print('-'*75)
# i can locate the index value by value of loadja
# locはkey
print('the loadja value has index=>',cal.loc['loadja'])
print('-'*75)
# ilocはvalue
print('this will print the value of index 4=>',cal.iloc[4])
print('*'*75)
print('this will print the value of index 4=>',cal2.iloc[4])

print('-'*75)
print('-'*75)
# if i input scalar values of 5 ill get o/p as 5.0 for all abcde
# scalar_series = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
scalar_series = pd.Series(5,index=['a','b','c','d','e'])
print(scalar_series) 
# print(scalar_series) 

first=pd.Series([1,2,3,4],index=['a','b','c','d'])
second=pd.Series([10,20,30,40],index=['a','b','c','d'])
print(first+second)
print(second)
print('-'*75)
second=pd.Series([10,20,30,40],index=['a','c','b','d'])
print(first+second)
print('-'*75)
print(second)
print('-'*75)

print('-'*75)
print('-'*75)
fir=pd.Series([1,2,3,4])
sec=pd.Series([10,20,30,40],index=['a','b','c','d'])
print(fir+sec)
print('-'*75)
print('-'*75)

#DataFrame
#DataFrame is 2D ds
olympic_list={'HostCity':['London','Beijing','Atthens','Sydney','Atlanta'],
                'Year':[2012,2008,2004,2000,1996],
                'NO.of Participating Countries':[205,204,201,200,197]}
store_here=pd.DataFrame(olympic_list)
print(store_here)

wwf={'winner':['john sena','undertaker','markly','jimmy','bigshow'],
    'year':[2010,2000,2005,2004,2008],
    'No.of belt they won':[3,4,2,1,3]}
so_table=pd.DataFrame(wwf)
print(so_table)

print('-'*75)
wwf={'winner':['john sena','undertaker','markly','jimmy','bigshow'],
    'year':[2010,2000,2005,2004,2008],
    'No.of belt they won':[3,4,2,1,3]}
wwf_with_dict={'john sena':{2010:3},'jimmy':{2004:1}}
store=pd.DataFrame(wwf_with_dict)
print(store)


no_countries_participated_series=pd.Series([205,206,201,204,208,201]        ,index=[2012,2001,2000,2004,2005,2007])
Countries_list=pd.Series(['London','mekka','kittu','juttiu,','sris','lohka'],index=[2012,2001,2000,2004,2005,2007])

i_want_put_them_in_data_frames=pd.DataFrame({'Host Cities':Countries_list,'No.of Participations':no_countries_participated_series})
print(i_want_put_them_in_data_frames)
 
