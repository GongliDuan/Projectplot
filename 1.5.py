# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 09:11:13 2015

@author: gduan
"""
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
import pandas as pd
from skimage import feature
from PIL import Image
import csv
global matrix
matrix=np.zeros((1200,1600))
def func(a,use):
    im = Image.open(a)
    temp=np.asarray(im)
    col=1600
    row=1200
    use=np.zeros((row,col))
    for i in range(0,1200):
        for j in range(0,1600):
            use[i,j]=temp[i,j,0]
            j=j+1
        i=i+1
        '''
    b = open('matrix.csv', 'w')
    c = csv.writer(b)
    c.writerows(use)
    b.close()
    '''
    matrix=use
    return matrix
def fit_func(x, a, b,c):
    return a*(x**1.5) + b*x+c       
'''
pic=np.zeros((1200,1600))
func('C:\Users\gduan\Desktop\New folder (2)\F-175 BT 3_F-175-1-1__2015-10-22_13-50-35.png',matrix)
'''
im = Image.open('C:\Users\gduan\Desktop\F-200 BT 3\F-200 BT 3_F-200-1-1__2016-03-07_08-13-59.png')
temp=np.asarray(im)
col=1600
row=1200
use=np.zeros((row,col))
red=np.zeros((row,col))
green=np.zeros((row,col))
blue=np.zeros((row,col))
for i in range(0,1200):
    for j in range(0,1600):
        red[i,j]=temp[i,j,0]
        green[i,j]=temp[i,j,1]
        blue[i,j]=temp[i,j,2]
        j=j+1
    i=i+1
use=0.2126*red+0.7152*green+0.0722*blue
'''
b = open('matrixall.csv', 'w')
c = csv.writer(b)
c.writerows(use)
b.close()
'''
r=range(0,1600)
test1=use[350,r]

plt.plot(r,test1)
plt.show
plt.close



x=np.array(range(0,1600))
y=np.array(test1)

params = curve_fit(fit_func, x, y)
plt.plot(x, y, 'rx', label='data')
plt.plot(x, fit_func(x, *params[0]), 'b-', label='fit') 
plt.show()

equation_first=params[0]
print equation_first

'''
Read All Files In One Path
path=''
dirs = os.listdir( path )
for file in dirs:
    func(file,use)
    fit_func(x,a,b,c)
    x=np.array(range(0,800))
    y=np.array(test1)
    params = curve_fit(fit_func, x, y)
    plt.plot(x, y, 'rx', label='data')
    plt.plot(x, fit_func(x, *params[0]), 'b-', label='fit') 
    plt.show()
'''






