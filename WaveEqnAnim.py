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
    return x*(L-x)
    
# Initial velocity
def g(x):
    return 0

# Fourier cosine coefficient
def A(n):
    return (2.0/L)*integrate.quad(lambda x: \
            f(x)*np.sin(n*np.pi*x/L),0,L)[0]

# Fourier sine coefficient
def B(n):
    return (2.0/n/np.pi/c)*integrate.quad(lambda x: \
            g(x)*np.sin(n*np.pi*x/L),0,L)[0]

# Generate N Fourier cosine coefficients.
a = [0] + [A(n) for n in range(1,N+1)]
# Generate N Fourier sine coefficients.
b = [0] + [B(n) for n in range(1,N+1)]

def U(x,t):
    s = 0
    for n in range(1,N+1):
        s+=a[n]*np.sin(n*np.pi*x/L) * np.cos(n*np.pi*c*t/L) \
                +b[n]*np.sin(n*np.pi*x/L) * np.sin(n*np.pi*c*t/L) 
    return s

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
