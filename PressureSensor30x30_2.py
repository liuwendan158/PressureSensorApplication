# -*- coding: utf-8 -*-


import serial
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import animation

zero = np.zeros((30,30))
df=pd.DataFrame(zero)
port = "COM20"
baud = 115200
temp = 0b101111
data = 0
header = 0

X=df.columns.values
Y=df.index.values
Z=df.values
x,y=np.meshgrid(X, Y)
cmd="COM6"
fig=plt.figure()
plt.axes().set_aspect('equal')
row=0

def init():
    ser.flush
    sns.heatmap(df, vmax=1000,cmap="plasma",cbar=False,square=True)
    
def animate(i):
    if cmd == 'exit':
        ser.close()
        exit()
    else:
        ser.flushInput()
        #print("Please Enter CMD")
        #cmd=input()
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
                    df.set_value(29-i, j, data)
            Z=df.values
            plt.contourf(x,y,Z, 50, cmap=plt.cm.jet,vmin=100, vmax=500) 
            plt.show()
            

ser = serial.Serial(port, baud, timeout=1)
if ser.isOpen():
     print(ser.name + ' is open...')
     
     
anim = animation.FuncAnimation(fig, animate,frames=11200,interval=10,repeat=False)
plt.show()




