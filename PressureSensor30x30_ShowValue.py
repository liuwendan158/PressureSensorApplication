# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:33:34 2017

@author: user
"""

import serial
import numpy as np
from time import time
import matplotlib.pyplot as plt
#from pylab import rcParams
import seaborn as sns

M=np.zeros((30,30))
port = "COM20"
baud = 115200
temp = 0b101111
data = 0
header = 0
PressureArray=[]
X=[x for x in range(30)]
Y=[y for y in range(30)]
x,y=np.meshgrid(X, Y)
cmd="COM6"
#fig=plt.figure()
#plt.axes().set_aspect('equal')
row=0
    
def animate():
    df = np.zeros((30,30))
    while 1:
        header=0
        data1=0
        while(header != 255):
            header = int.from_bytes(ser.read(1),'big')
        data1=ser.read(1)
        if(data1==b'\xff'):
            for i in range(30):
                for j in range(30):
                    temp =ser.read(2)
                    data=int.from_bytes(temp,byteorder='little')
                    df[29-i,j] = data
            #plt.contourf(x,y,df, 50, cmap=plt.cm.jet,vmin=0, vmax=700)                             
            #plt.show()
            yield df

ser = serial.Serial(port, baud, timeout=1)
if ser.isOpen():
     print(ser.name + ' is open...')

rw=animate()
M=next(rw)
past=time()


for i in range(60000):
    plt.clf()
    M=next(rw)
    sns.heatmap(M, vmax=1000,cmap="plasma",cbar=True,square=True)
    plt.show()
    plt.pause(0.03)
    rightnow=time()