import matplotlib.pyplot as plt
import numpy as np

# 1. Set up a 2D spatial coordinate grid for the black hole accretion disk
x, y = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))

# 2. Define the plasma velocity vector field (Keplerian rotation loops)
v_x, v_y = -y / (x**2 + y**2 + 1), x / (x**2 + y**2 + 1)

# 3. Define the magnetic field vector lines stretching outward
b_x, b_y = x * 0.2, y * 0.2

print("--- INITIALIZING RMHD PLASMA INDUCTION ENGINE ---")

# 4. Plot the interaction spatially
plt.quiver(x, y, v_x, v_y, color='blue', label='Plasma Flow Vector (v)', alpha=0.6)
plt.quiver(x, y, b_x, b_y, color='crimson', label='Magnetic Field Lines (B)', alpha=0.6)
plt.title("Visualizing Keya's Diary Page 6: MHD Fluid Matrix")
plt.xlabel("X Coordinate"); plt.ylabel("Y Coordinate"); plt.legend(); plt.show()
