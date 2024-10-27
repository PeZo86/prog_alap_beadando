import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from pandas.core.common import random_state
from sklearn.linear_model import LinearRegression

#Get dataset
df_sal = pd.read_csv('ele0033.csv')
df_sal.head()

#describe data
df_sal.describe()

#data distribution
plt.title('Salary Distribution Plot')
sns.distplot(df_sal['Relatív jövedelmi szegénységi arány'])
plt.show()

#Relationship
plt.scatter(df_sal['Referencia év'], df_sal['Relatív jövedelmi szegénységi arány'], color = 'lightcoral')
plt.title('Salary vs Experience')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.box(False)
plt.show()