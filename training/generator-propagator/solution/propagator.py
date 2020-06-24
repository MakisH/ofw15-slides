import numpy as np
import matplotlib.pyplot as plt
import precice


n = 20
dn = 1 / n

# generate mesh
x = np.linspace(0, 1, n+1)
y = np.linspace(0, 1, n+1)

# initial data, associated to cell centers
u = np.zeros([n, n])

# preCICE setup
participant_name = "Propagator"
config_file_name = "precice-config.xml"
solver_process_index = 0
solver_process_size = 1
interface = precice.Interface(participant_name, config_file_name, solver_process_index, solver_process_size)

mesh_name = "Propagator-Mesh"
mesh_id = interface.get_mesh_id(mesh_name)

data_name = "Data"
data_id = interface.get_data_id(data_name, mesh_id)

vertices = [[1, y0] for y0 in y[:-1]]

vertex_ids = interface.set_mesh_vertices(mesh_id, vertices)

precice_dt = interface.initialize()

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

t = 0

while interface.is_coupling_ongoing():

  dt = 0.0025
  
  print("Propagating data")
  dt = np.minimum(dt, precice_dt)
  
  u[:,-1] = interface.read_block_scalar_data(data_id, vertex_ids)
  
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
  
  precice_dt = interface.advance(dt)

  # advance  
  t = t + dt 
    
interface.finalize()
