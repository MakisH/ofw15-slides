import numpy as np
import matplotlib.pyplot as plt

n = 20
dn = 1 / n

# generate mesh
x = np.linspace(0, 1, n+1)
y = np.linspace(0, 1, n+1)

# initial data, associated to cell centers
u = np.zeros([n, n])

# plot initial data
fig = plt.figure()
ax = fig.add_subplot(111)
X, Y = np.meshgrid(x, y)
c = ax.pcolor(X, Y, u, vmin=-1, vmax=1, edgecolors='k', linewidths=1, cmap='RdBu')
fig.colorbar(c, ax=ax)
plt.axvspan(0.99, 1.0, color='grey', alpha=0.8)
plt.xlabel("x (Interface at x=1)")
plt.ylabel("y")
plt.ion()
plt.show()

dt = 0.01
t = 0

# some data to propagate, "-1" in Python means the last entry
u[:,-1] = y[:-1] 

while True:
  
  print("Propagating data")
  # some (arbitrary) convection-diffusion rule
  # top row
  u[0, :-1] = 0.3 * u[0, :-1] + 0.6 * u[0, 1:] + 0.1 * u[1, :-1] 
  # inner domain
  u[1:-1, :-1] = 0.2 * u[1:-1, :-1] + 0.6 * u[1:-1, 1:] + 0.1 * u[2:, :-1] + 0.1 * u[:-2, :-1]
  # bottom row
  u[-1, :-1] = 0.3 * u[-1, :-1] + 0.6 * u[-1, 1:] + 0.1 * u[-1, :-1]

  # plot current result
  plt.pause(0.2)  
  ax.pcolor(X, Y, u, vmin=-1, vmax=1, edgecolors='k', linewidths=1, cmap='RdBu')

  # advance  
  t = t + dt 
  if(t > 0.2):
    break
