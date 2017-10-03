# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:36:00 2017

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 13:20:37 2017

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:47:03 2017

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:04:08 2017

@author: user
"""

import serial
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import animation

zero = np.zeros((30,30))
df=pd.DataFrame(zero)
port = "COM6"
baud = 115200
temp = 0b101111
data = 0
header = 0

x=[0,1,2,3,4,5,6]
y=[0,1,2,3,4,5,6,7,8,9]
cmd="COM6"
fig=plt.figure()
#flashdata=[]
#leng=0
row=0


    #sns.heatmap(df, vmax=1000,cmap="plasma",cbar=False,square=True)



ser = serial.Serial(port, baud, timeout=1)
if ser.isOpen():
     print(ser.name + ' is open...')
     
'''while(ser.in_waiting>0):
    for i in (leng,leng+ser.in_waiting)
        flashdata[i]=ser.read();'''

#anim = animation.FuncAnimation(fig, animate, init_func=init,frames=112000, repeat = False)
#plt.show()
while True:
  if cmd == 'exit':
     ser.close()
     exit()
  else:
        #ser.flushInput()
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
                df.set_value(i, j, data)
        sns.heatmap(df, vmax=300,cmap="plasma",cbar=False,square=True)
        fig.canvas.draw()
        plt.show()

