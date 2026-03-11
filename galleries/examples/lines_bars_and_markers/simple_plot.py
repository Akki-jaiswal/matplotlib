"""
=========
Line plot
=========

Create a basic line plot with enhanced styling and saving capabilities.
"""

import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# Creating the figure and axis with explicit size for better visibility
fig, ax = plt.subplots(figsize=(8, 5))

# Plotting the data with styled properties
ax.plot(t, s, color='tab:blue', linewidth=2.5, label='Sine wave')

# Setting axis labels and title
ax.set(xlabel='Time (s)', 
       ylabel='Voltage (mV)',
       title='Basic Sine Wave Plot')

# Adding a styled grid for easier data reading
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Adjust layout to prevent label clipping
plt.tight_layout()

# Save the figure to a file (optional but good practice)
plt.savefig('sine_wave.png', dpi=300, bbox_inches='tight')

plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`
#    - `matplotlib.pyplot.subplots`
#    - `matplotlib.figure.Figure.savefig`
#
# .. tags::
#
#    plot-type: line
#    level: beginner
