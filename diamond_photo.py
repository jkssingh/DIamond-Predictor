import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea

dataset=pd.read_csv('diamonds.csv')
dataset=dataset.drop('Unnamed: 0',axis=1)
dataset2=dataset.drop('price',axis=1)

corr=dataset.corr()
sea.heatmap(data=corr,square=True,annot=True,cbar=True)

sea.factorplot(data=dataset2,kind='box')
plt.xlabel('attributes')

#for i in range(0,len(dataset)):
#    if(dataset.loc[i,'carat']>0 and dataset.loc[i,'carat']<1):
#        dataset.loc[i,'carat']=0
#    elif(dataset.loc[i,'carat']>=1 and dataset.loc[i,'carat']<2):
#        dataset.loc[i,'carat']=1
#    elif(dataset.loc[i,'carat']>=2 and dataset.loc[i,'carat']<3):
#        dataset.loc[i,'carat']=2
#    elif(dataset.loc[i,'carat']>=3 and dataset.loc[i,'carat']<4):
#        dataset.loc[i,'carat']=3
#    elif(dataset.loc[i,'carat']>=4 and dataset.loc[i,'carat']<5):
#        dataset.loc[i,'carat']=4
#    elif(dataset.loc[i,'carat']>=5 and dataset.loc[i,'carat']<6):
#        dataset.loc[i,'carat']=5
#    

#carat and price
plt.hist(dataset.carat)
sea.lmplot(x='carat',y='price',data=dataset,fit_reg=False)
plt.title('Carat vs Price')
sea.lmplot(x='carat',y='price',data=dataset,fit_reg=False,hue='color')
plt.title('Carat vs Price with color')
sea.lmplot(x='carat',y='price',data=dataset,fit_reg=False,hue='cut')
plt.title('Carat vs Price with cut')
sea.lmplot(x='carat',y='price',data=dataset,fit_reg=False,hue='clarity')
plt.title('Carat vs Price with clarity')
sea.distplot(dataset.carat)
#sea.jointplot(x='carat' , y='price' , data=dataset , size=5) 

#cut and price
sea.countplot(x='cut', data=dataset)
plt.title('Diamond Cut')
plt.hist(dataset.cut)
sea.boxplot(x='cut',y='price',data=dataset)
plt.title('Cut vs Price')
sea.set_style('whitegrid')
sea.violinplot(x='cut',y='price',data=dataset)
plt.title('Cut vs Price')
#color and price
sea.countplot(x='color',data=dataset)
plt.title('Diamond Color')
sea.boxplot(x='color',y='price',data=dataset)
plt.title('Color vs Price')
sea.set_style('whitegrid')
sea.violinplot(x='color',y='price',data=dataset)
plt.title('Color vs Price')
#clarity and price
sea.countplot(x='clarity',data=dataset)
plt.title('Diamond Clarity')
sea.boxplot(x='clarity',y='price',data=dataset)
plt.title('Clarity vs Price')
sea.set_style('whitegrid')
sea.violinplot(x='clarity',y='price',data=dataset)
plt.title('Clarity vs Price')
#depth and price
plt.hist(dataset.depth)
sea.lmplot(x='depth', y='price', data=dataset,fit_reg=False)
plt.title('Depth vs Price')
sea.lmplot(x='depth',y='price',data=dataset,fit_reg=False,hue='color')
plt.title('Depth vs Price with color')
sea.lmplot(x='depth',y='price',data=dataset,fit_reg=False,hue='cut')
plt.title('Depth vs Price with cut')
sea.lmplot(x='depth',y='price',data=dataset,fit_reg=False,hue='clarity')
plt.title('Depth vs Price with clarity')

#table and price
plt.hist(dataset.table)
sea.lmplot(x='table', y='price', data=dataset,fit_reg=False)
plt.title('Table vs Price')
sea.lmplot(x='table',y='price',data=dataset,fit_reg=False,hue='color')
plt.title('Table vs Price with color')
sea.lmplot(x='table',y='price',data=dataset,fit_reg=False,hue='cut')
plt.title('Table vs Price with cut')
sea.lmplot(x='table',y='price',data=dataset,fit_reg=False,hue='clarity')
plt.title('Table vs Price with clarity')

#x*y*z and price
sea.kdeplot(dataset.x,shade=True,color='red')
sea.kdeplot(dataset.y,shade=True,color='green')
sea.kdeplot(dataset.z,shade=True,color='blue')
plt.xlim(0,9)
