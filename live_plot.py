import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates
import numpy as np
import datetime

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("live_tweet.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    ytmp   = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y= eachLine.split('$#%#')         
            xar.append(datetime.datetime.fromtimestamp(float(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))
            ytmp.append(float(y))
            yar.append(np.mean(ytmp))
    
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
    ax1.xaxis_date()
    ax1.plot(xar,yar)
    for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
    

ani = animation.FuncAnimation(fig, animate, interval=1)
plt.subplots_adjust(bottom=.23)
plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
plt.grid(True)
plt.show()

