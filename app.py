import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Slider

#X = Asin(ax+b)
#Y = Asin(cx+d)

#variable
A = 1
B = 1
a = 1
b = 0
c = 1
d = 0

#rate for change variable
rA = 0
rB = 0
ra = 0
rb = 0
rc = 0
rd = 0

#countiue the graph
count = 0

#X position for point
position = 100

# change the variable as per changing rate
def change_variable():
    pass
    global A
    global B
    global a
    global b
    global c
    global d
    global rA
    global rB
    global ra
    global rb
    global rc
    global rd

    if A<=0.5 or A>=1.5:
       rA = -rA
    if B<=0.5 or B>=1.5:
        rB = -rB
    if a<=0.5 or a>=3.5:
        ra = -ra
    if c<=0.5 or c>=3.5:
        rc = - rc
    if b<=-2.5 or b>=2.5:
        rb = -rb
    if d<=-2.5 or d>=2.5:
        rd = -rd
    A += rA
    B += rB
    a += ra
    c += rc
    b += rb
    d += rd


fig, ax = plt.subplots(figsize=(18, 12))
plt.subplots_adjust(left=0, bottom=0.3, right=1, top=0.95, wspace=0, hspace=0)
ax.axis('square')
ax.set_xlim((0, 25))
ax.set_ylim((-4, 21))
ax.set_title("2 Wave merging simulation imagenory plane")
linex, = ax.plot([], [], label = 'X=Asin(ax+b)')
liney, = ax.plot([], [], label = 'Y=Bsin(cx+d)')
line_final, = ax.plot([], [], label = 'X+Y')
point, = ax.plot([], [],'--',marker = 'o')


#variables's widgets's position(right side widgets)
xamp = plt.axes([0.70, 0.9, 0.25, 0.05])
yamp = plt.axes([0.70, 0.8, 0.25, 0.05])
xfreq = plt.axes([0.70, 0.7, 0.25, 0.05])
yfreq = plt.axes([0.70, 0.6, 0.25, 0.05])
xphase = plt.axes([0.70, 0.5, 0.25, 0.05])
yphase = plt.axes([0.70, 0.4, 0.25, 0.05])
point_position = plt.axes([0.70, 0.3, 0.25, 0.05])

#change in variable's widgets's position(left side widgets)
rxamp = plt.axes([0.04, 0.9, 0.25, 0.05])
ryamp = plt.axes([0.04, 0.8, 0.25, 0.05])
rxfreq = plt.axes([0.04, 0.7, 0.25, 0.05])
ryfreq = plt.axes([0.04, 0.6, 0.25, 0.05])
rxphase = plt.axes([0.04, 0.5, 0.25, 0.05])
ryphase = plt.axes([0.04, 0.4, 0.25, 0.05])

linex.set_data([], [])
liney.set_data([], [])
line_final.set_data([], [])
point.set_data([], [])

#right side widgets
sxamp = Slider(xamp, 'A', 0, 2, valinit=A)
syamp = Slider(yamp, 'B', 0, 2, valinit=B)
sxfreq = Slider(xfreq, 'a', 0, 4, valinit=a)
syfreq = Slider(yfreq, 'c', 0, 4, valinit=c)
sxphase = Slider(xphase, 'b', -np.pi, np.pi, valinit=b)
syphase = Slider(yphase, 'd', -np.pi, np.pi, valinit=d)
spoint_position = Slider(point_position, 'point', 0, 24, valinit=position/20)

#left side widgets
srxamp = Slider(rxamp, 'rate_A', 0, 0.5, valinit=rA)
sryamp = Slider(ryamp, 'rate_B', 0, 0.5, valinit=rB)
srxfreq = Slider(rxfreq, 'rate_a', 0, 0.5, valinit=ra)
sryfreq = Slider(ryfreq, 'rate_c', 0, 0.5, valinit=rc)
srxphase = Slider(rxphase, 'rate_b', 0, 0.5, valinit=rb)
sryphase = Slider(ryphase, 'rate_d', 0, 0.5, valinit=rd)


#animation function
def animate(i):
    # not creating exctra variable using global variables
    global A
    global B
    global a
    global b
    global c
    global d
    global position
    global count

    #plot the graph
    temp = np.linspace(count, 25+count, 500)
    x = temp - count
    X_graph = 13 + A*np.sin(a*temp+b)
    Y_graph = 7 + B*np.sin(c*temp+d)
    final_graph = X_graph + Y_graph-19
    linex.set_data(x, X_graph)
    liney.set_data(x, Y_graph)
    line_final.set_data(x,final_graph)
    point.set_data([x[position],x[position],x[position]],[X_graph[position],Y_graph[position],final_graph[position]])
    count += 0.1

    #to change variable as per changing rate
    change_variable()

#start animation
anim = animation.FuncAnimation(fig, animate,frames=400, interval=3)


#Execute when any variable slider's value changes
def update(val):
    # not creating exctra variable using global variables
    global anim
    global A
    global B
    global a
    global b
    global c
    global d
    global position

    # set velue of sliders to variable
    A = sxamp.val
    B = syamp.val
    a = sxfreq.val
    c = syfreq.val
    b = sxphase.val
    d = syphase.val
    position = int(spoint_position.val*20)

    fig.canvas.draw_idle()

#Execute when any variable rate slider's value changes
def change_rate(val):
    global anim
    global rA
    global rB
    global ra
    global rb
    global rc
    global rd
    global position
    rA = srxamp.val
    rB = sryamp.val
    ra = srxfreq.val
    rc = sryfreq.val
    rb = srxphase.val
    rd = sryphase.val

    #get all value zero set a variable sliders's value
    if rA==0 and rB == 0 and ra == 0 and rb == 0 and rc == 0 and rd == 0:
        update(0)
    # get all value o.5 set a variable sliders's value to reduce problem
    # to see the problem remove or comment next two lines
    if rA==0.5 and rB == 0.5 and ra == 0.5 and rb == 0.5 and rc == 0.5 and rd == 0.5:
        update(0)
    fig.canvas.draw_idle()

sxamp.on_changed(update)
syamp.on_changed(update)
sxfreq.on_changed(update)
syfreq.on_changed(update)
sxphase.on_changed(update)
syphase.on_changed(update)
spoint_position.on_changed(update)

srxamp.on_changed(change_rate)
sryamp.on_changed(change_rate)
srxfreq.on_changed(change_rate)
sryfreq.on_changed(change_rate)
srxphase.on_changed(change_rate)
sryphase.on_changed(change_rate)

ax.legend(fontsize=12)
plt.show()
