# All of the other examples directly embed the Javascript and CSS code for
# Bokeh's client-side runtime into the HTML.  This leads to the HTML files
# being rather large.  An alternative is to ask Bokeh to produce HTML that
# has a relative link to the Bokeh Javascript and CSS.  This is easy to
# do; you just pass in a few extra arguments to the output_file() command.

import numpy as np
from bokeh.plotting import *

N = 100
x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)

output_file("relative.html", title="Relative path example",
        js="relative", css="relative")

scatter(x,y, color="#FF00FF", tools="pan,wheel_zoom,resize,save")

show()

# By default, the URLs for the Javascript and CSS will be relative to
# the current directory, i.e. the directory in which the HTML file is
# generated.  You can provide a different "root" directory from which
# the relative paths will be computed:
#
#output_file("scatter.html", title="scatter.py example",
#        js="relative", css="relative", rootdir="/some/other/path")

