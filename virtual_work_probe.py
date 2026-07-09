import matplotlib.pyplot as plt
import numpy as np

# 1. Map out a physical V-shaped valley profile (Potential Energy Grid)
x_valley = np.linspace(-5, 5, 100)
y_valley = x_valley ** 2  # Parabolic structural boundary

# 2. Position of our stable particle at the absolute minimum (0,0)
particle_x, particle_y = 0, 0

# 3. Simulate a tiny virtual "ghost displacement" vector along the constraint
virtual_dx = 0.5
virtual_dy = 0.0  # Infinitesimal shift probe

# 4. Graph the spatial matrix
plt.plot(x_valley, y_valley, label="Constraint Valley Boundary", color="purple")
plt.scatter(particle_x, particle_y, color="red", s=120, label="Stable Equilbrium (System Core)")
plt.arrow(particle_x, particle_y, virtual_dx, virtual_dy, head_width=0.2, color="gold", label="Virtual Shift Probe")
plt.title("Visualizing D'Alembert's Virtual Work Vector"); plt.legend(); plt.grid(True); plt.show()
