'''
import numpy, glumpy
from glumpy.pylab import *

window = glumpy.Window(256,64)
Z = data.astype(numpy.float32)

t0, frames, t = 0,0,0
fig = plt.figure(figsize=(7,7))
ax = plt.subplot(111)
ax = imshow(Z[:,:,0], origin='lower', interpolation='bilinear')
show()
window = glumpy.active_window()

@window.event
def on_idle(dt):    
    global Z, t0, frames, t

    t += dt
    frames = frames + 1
    if frames > 248:
        fps = float(frames)/(t-t0)
        print('FPS: %.2f (%d frames in %.2f seconds)' ,% (fps, frames, t-t0))
        frames,t0 = 0, t

    for image, axis, alpha in items:
        image.data[...] = Z[:,:,frames]
        image.update()
    window.draw()

window.mainloop()'''


import serial
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import glumpy


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
    sns.heatmap(df, vmax=1000,cmap="plasma",cbar=False,square=True)
    
def animate():
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
                    df.set_value(29-i, j, data)
            Z=df.values
            plt.contourf(x,y,Z, 50, cmap=plt.cm.jet,vmin=0, vmax=700)                             
            plt.show()

ser = serial.Serial(port, baud, timeout=1)
if ser.isOpen():
     print(ser.name + ' is open...')

   

window = glumpy.Window(30,30)

@window.event
def on_draw():
    #window.clear()
    animate()
    
#window.mainloop()


