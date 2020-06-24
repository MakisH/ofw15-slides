import numpy as np
import time


n = 20
dn = 1 / n

# generate mesh
y = np.linspace(0, 1, n + 1)

dt = 0.01
t = 0

while True:
  
  print("Generating data")
  time.sleep(0.2)
  u = 1 - 2 * np.random.rand(n)
  
  t = t + dt 
  if(t > 0.1):
    break
  
