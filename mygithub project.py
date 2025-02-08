import pandas as pd
from pandas import DataFrame
import numpy as np

data=DataFrame({'Names':['Shyaka',None,'Manzi'],
                'Age':[12,np.nan,13]})
data['Names']=data['Names'].fillna('Unknown')
data['Age']=data['Age'].fillna('invalid')
print(data)

