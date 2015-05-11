import scipy.integrate as integrate
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Follows example in Section 4.4 in Haberman 5th.  Wave equation,
# u(x,0)=f(x), u_t(x,0)=g(x),  u(0,t)=u(L,t)=0

# Plot resolution, number of points in interval partition.
R=200

# Number of terms to generate.
N=40

# Length of string
L=1

# wave speed
c=1

# Initial position
def f(x):
    if x>=.25 and x<=.75: 
        return 1
    else: 
        return 0

def fo(x):
    return (f(x)-f(-x))/2.0

def F(x):
    return fo(x-np.floor((x+L)/2/L)*2*L)
    
def U(x,t):
    return (F(x-c*t) + F(x+c*t))/2.0

# Animate Fourier series and initial temp distribution.
# First set up the figure, the axis, and the plot element we want to
# animate
fig = plt.figure()
ax = plt.axes(xlim=(0, L), ylim=(-1, 1))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, L, 1000)
    t = [U(p,i/50) for p in x]
    line.set_data(x, t)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20, blit=True)

#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()
