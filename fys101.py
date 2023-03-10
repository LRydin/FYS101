__name__ = "fys101"
__version__ = "0.0.1"
__author__ = "Leonardo Rydin Gorjão & Heidi Nygård"
__copyright__ = "Copyright NMBU"

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

import logging
logging.getLogger('matplotlib.font_manager').disabled = True

__all__ = [
    'projectile_motion',
]

print('Welcome to FYS101: Mechanics with Python')
print('                  ....                  ')
print(' --  Current modules in fys101 are:  -- ')
[print('  ' + a + '()') for a in __all__]

def projectile_motion(g = 9.80665):

    # The parametrized function to be plotted
    def f(x, v, phi):
        return x * np.tan(np.radians(phi)) \
            - ((g*x**2)/(2* v **2 * np.cos(np.radians(phi))**2))

    def d(v, phi):
        return ((2 * v * np.sin(np.radians(phi))) / g ) * np.cos(np.radians(phi)) * v


    x = np.linspace(0, 15, 1000)

    # Create the figure and the line that we will manipulate
    # with plt.xkcd():
    fig, ax = plt.subplots(figsize=(6,3.5))
    line, = ax.plot(x, f(x, 8, 20), ':', color='k', lw=2)

    dot, = ax.plot(d(8, 20), 0, marker='o', ms=10, color='red', lw=2)

    text_ = ax.text(s='Distance: {:.2f}'.format(d(8, 20)), x=7.5, y=7,
        color='red', ha='center', fontsize=14)

    ax.set_xlabel('Distance [m]')
    ax.set_ylabel('Height [m]')
    ax.set_ylim([0,8])
    # adjust the main plot to make room for the sliders
    fig.subplots_adjust(left=0.25, bottom=0.25)

    # Make a horizontal slider to control the frequency.
    ax_vel = fig.add_axes([0.25, 0.03, 0.65, 0.03])
    vel_slider = Slider(
        ax=ax_vel,
        label='Velocity [m/s]',
        valmin=0.1,
        valmax=12,
        valinit=8,
        valstep=0.1,
    )

    # Make a vertically oriented slider to control the amplitude
    ax_degree = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
    degree_slider = Slider(
        ax=ax_degree,
        label=r'Angle [º]',
        valmin=0,
        valmax=89,
        valinit=20,
        valstep=1,
        orientation='vertical'
    )

    # The function to be called anytime a slider's value changes
    def update(val):
        line.set_ydata(f(x, vel_slider.val, degree_slider.val))
        dot.set_xdata(d(vel_slider.val, degree_slider.val))
        text_.set_text('Distance: {:.2f}'.format(d(vel_slider.val, degree_slider.val)))
        fig.canvas.draw_idle()

    # register the update function with each slider
    vel_slider.on_changed(update)
    degree_slider.on_changed(update)

    return plt.show()
