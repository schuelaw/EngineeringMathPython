import scipy.integrate as integrate
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Follows example in Section 2.3 in Haberman 5th.  Heat equation,
# u(x,0)=f(x), u(0,t)=u(L,t)=0

# Plot resolution, number of points in interval partition.
R=200

# Number of terms to generate.
N=20

# Length of rod
L=1

# Conductivity
k=1

# Initial temperature distribution.
def f(x):
    if x>0.25 and x<0.75: return x
    else: return 0

# mth Fourier sine coefficient, eq 2.3.35
def B(m):
    return (2.0/L)*integrate.quad(lambda x: \
            f(x)*np.cos(m*np.pi*x/L),0,L)[0]

# Generate the 0th coeff:
b=[B(0)/2.0]

# Generate remaining N Fourier cosine coefficients.
for m in range(1,N+1): b.append(B(m))

def U(x,t):
    s = 0
    for i in range(N+1):
        s+=b[i]*np.cos(i*np.pi*x/L)*np.exp(-(i*np.pi/L)**2*k*t)
    return s

# Animate Fourier series and initial temp distribution.
# First set up the figure, the axis, and the plot element we want to
# animate
fig = plt.figure()
ax = plt.axes(xlim=(0, L), ylim=(-0.1, 1))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, L, 1000)
    y = [U(p,i/600) for p in x]
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()
