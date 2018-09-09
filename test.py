import sys
#sys.path.append('/home/nouman/anaconda2/envs/tensorflow/lib/python2.7/site-packages')
import numpy as np
#import tensorflow as tf
#import cv2
import pandas as pd
from matplotlib.pyplot import matplotlib
from matplotlib import style
style.use('fivethirtyeight')

col = ['d','v']
df =pd.read_csv('test.csv',header=None, names=col, na_values=['Value','Date'], parse_dates=[[0,1]])
df['new'] = 0
#df.columns = ['hhhh']
#df.to_csv('newcsv.csv', header=False)
#df = pd.read_csv('newcsv.csv',names=['date','value'])

#f.rename(columns={'value':'great', 'date':'time'}, inplace=True)
#df.set_index('Value', inplace=True)
#df.to_html('htmlt.html')
df.insert(1,'hi', 15)
df.index = df['hi']
df.index.name = 'he;lllo'
x = df['new'].values
#df = pd.read_csv('newcsv2.csv', index_col=0)]
print x

