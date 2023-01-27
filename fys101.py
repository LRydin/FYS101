__name__ = "fys101"
__version__ = "0.0.1"
__author__ = "Leonardo Rydin Gorjão & Heidi Nygård"
__copyright__ = "Copyright NMBU"

import numpy as np

from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import figure, show

from bokeh.io import output_notebook
output_notebook()

__all__ = [
    'projectile_motion',
]

print('Welcome to FYS101: Mechanics with Python')
print('                  ....                  ')
print('   Current modules in fys101 are:')
[print('   ' + a + '()') for a in __all__]

def projectile_motion():
    x = np.linspace(0, 15, 5000)

    g=9.80665
    angle = 20
    velocity = 8
    y = x * np.tan(np.radians(angle)) - ((g*x**2)/(2* velocity ** 2 * np.cos(np.radians(angle))**2))

    source = ColumnDataSource(data=dict(x=x, y=y))

    plot = figure(y_range=(0, 8), width=250, height=250, toolbar_location=None)

    plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

    velocity = Slider(start=0.1, end=12, value=8, step=.1, title="Velocity")
    angle = Slider(start=0, end=90, value=20, step=1, title="Angle")

    callback = CustomJS(args=dict(source=source, velocity=velocity, angle=angle),
                        code="""
        const g = 9.80665
        const v = velocity.value
        const phi = angle.value

        const x = source.data.x
        const y = Array.from(x, (x) => x * Math.tan(Math.radians(phi)) - ((g*x**2)/(2* v **2 * Math.cos(Math.radians(phi))**2)))
        source.data = { x, y }
    """)

    velocity.js_on_change('value', callback)
    angle.js_on_change('value', callback)

    output_notebook()

    return show(row(plot, column(velocity, angle)))
