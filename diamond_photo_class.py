import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea

dataset=pd.read_csv('diamonds.csv')
dataset=dataset.drop('Unnamed: 0',axis=1)
dataset2=dataset.drop('price',axis=1)

class carat_price():
    
    def hist(self):
         sea.distplot(dataset.carat,kde=False)

    def implot_colorless(self):
        sea.lmplot(x='carat',y='price',data=dataset,fit_reg=False)
        plt.title('Carat vs Price')
        
    def implot_color_color(self):
        sea.lmplot(x='carat',y='price',data=dataset,fit_reg=False,hue='color')
        plt.title('Carat vs Price with color')
        
    def implot_color_cut(self):
        sea.lmplot(x='carat',y='price',data=dataset,fit_reg=False,hue='cut')
        plt.title('Carat vs Price with cut')

    def implot_color_clarity(self):
        sea.lmplot(x='carat',y='price',data=dataset,fit_reg=False,hue='clarity')
        plt.title('Carat vs Price with clarity')
    
    def distplot(self):
        sea.distplot(dataset.carat)

class cut_price():
    
    def countplot(self):
        sea.countplot(x='cut', data=dataset)
        plt.title('Diamond Cut')
        
    def boxplot(self):
        sea.factorplot(x='cut',y='price',data=dataset,kind='box')
        plt.title('Cut vs Price')

    def violinplot(self):
        sea.factorplot(x='cut',y='price',data=dataset,kind='violin')
        plt.title('Cut vs Price 2')

class color_price():
    
    def countplot(self):
        sea.countplot(x='color',data=dataset)
        plt.title('Diamond Color')

    def boxplot(self):
        sea.factorplot(x='clarity',y='price',data=dataset,kind='box')
        plt.title('Color vs Price')

    def violinplot(self):
        sea.factorplot(x='color',y='price',data=dataset,kind='violin')
        plt.title('Color vs Price')
        
class clarity_price():
    
    def countplot(self):
        sea.countplot(x='clarity',data=dataset)
        plt.title('Diamond Clarity')
        
    def boxplot(self):
        sea.factorplot(x='clarity',y='price',data=dataset,kind='box')
        plt.title('Clarity vs Price')

    def violinplot(self):
        sea.factorplot(x='clarity',y='price',data=dataset,kind='violin')
        plt.title('Clarity vs Price')

class depth_price():
    
    def hist(self):
         sea.distplot(dataset.depth,kde=False)

    def implot_colorless(self):
        sea.lmplot(x='depth', y='price', data=dataset,fit_reg=False)
        plt.title('Depth vs Price')
    
    def implot_color_color(self):
        sea.lmplot(x='depth',y='price',data=dataset,fit_reg=False,hue='color')
        plt.title('Depth vs Price with color')

    def implot_color_cut(self):
        sea.lmplot(x='depth',y='price',data=dataset,fit_reg=False,hue='cut')
        plt.title('Depth vs Price with cut')

    def implot_color_clarity(self):
        sea.lmplot(x='depth',y='price',data=dataset,fit_reg=False,hue='clarity')
        plt.title('Depth vs Price with clarity')
            
    def distplot(self):
        sea.distplot(dataset.depth)

class table_price():
    
    def hist(self):
         sea.distplot(dataset.table,kde=False)

    def implot_colorless(self):
        sea.lmplot(x='table', y='price', data=dataset,fit_reg=False)
        plt.title('Table vs Price') 
    
    def implot_color_color(self):
        sea.lmplot(x='table',y='price',data=dataset,fit_reg=False,hue='color')
        plt.title('Table vs Price with color')

    def implot_color_cut(self):
        sea.lmplot(x='table',y='price',data=dataset,fit_reg=False,hue='color')
        plt.title('Table vs Price with color')

    def implot_color_clarity(self):
        sea.lmplot(x='table',y='price',data=dataset,fit_reg=False,hue='clarity')
        plt.title('Table vs Price with clarity')
            
    def distplot(self):
        sea.distplot(dataset.table)

class xyz_price():
    
    def kdeplot(self):
        sea.kdeplot(dataset.x,shade=True,color='red')
        sea.kdeplot(dataset.y,shade=True,color='green')
        sea.kdeplot(dataset.z,shade=True,color='blue')
        plt.xlim(0,9)
