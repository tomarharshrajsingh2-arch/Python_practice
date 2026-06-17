import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

df=pd.DataFrame({
'Marks': np.random.randint(40,100,100),
'Study_hours':np.random.uniform(2,10,100),
'City':np.random.choice(['Bhopal','Indore','Jabalpur'],100),
'gender': np.random.choice(['male','female'],100)

})

# plt.figure(figsize=(10,4))
# sns.histplot(df['Marks'],bins=20,kde=True,color='steelblue')
# plt.title('Distribution of student marks')
# plt.show()

##BOX PLOT
# sns.boxplot(data=df,x='City',y='Marks',palette='Set2')
# plt.title('Marks distribution by city')
# plt.show()

##Heat map

# plt.figure(figsize=(5,4))
# sns.heatmap(df[['Marks','Study_hours']].corr(),annot=True,cmap='coolwarm',vmin=-1,vmax=1)
# plt.title('corelation matrix')
# plt.show()

##pair plot
sns.pairplot(df[['Marks','Study_hours']], diag_kind='kde')
plt.show()
