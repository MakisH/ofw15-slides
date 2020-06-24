import numpy as np
import time
import precice


n = 20
dn = 1 / n

# generate mesh
y = np.linspace(0, 1, n + 1)

# preCICE setup
participant_name = "Generator"
config_file_name = "precice-config.xml"
solver_process_index = 0
solver_process_size = 1
interface = precice.Interface(participant_name, config_file_name, solver_process_index, solver_process_size)

mesh_name = "Generator-Mesh"
mesh_id = interface.get_mesh_id(mesh_name)

data_name = "Data"
data_id = interface.get_data_id(data_name, mesh_id)

vertices = [[1, y0] for y0 in y[:-1]]

vertex_ids = interface.set_mesh_vertices(mesh_id, vertices)

precice_dt = interface.initialize()

dt = 0.01
t = 0

while interface.is_coupling_ongoing():
  
  print("Generating data")
  dt = np.minimum(dt, precice_dt)
  time.sleep(0.2)
  u = 1 - 2 * np.random.rand(n)
  
  interface.write_block_scalar_data(data_id, vertex_ids, u)
  
  precice_dt = interface.advance(dt)
  
  t = t + dt 
  
interface.finalize()

