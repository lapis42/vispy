# -*- coding: utf-8 -*-
# Copyright (c) 2015, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

"""
Demonstration of PolygonVisual, EllipseVisual, RectangleVisual
and RegularPolygon
"""

from vispy import app
import sys
from vispy.scene import SceneCanvas
from vispy.scene.visuals import Polygon, Ellipse, Rectangle, RegularPolygon
from vispy.color import Color



white = Color("#ecf0f1")
gray = Color("#121212")
red = Color("#e74c3c")
blue = Color("#2980b9")
orange = Color("#e88834")

canvas = SceneCanvas(keys='interactive', title='Polygon Example',
                     show=True)
v = canvas.central_widget.add_view()
v.bgcolor = gray
v.camera = 'panzoom'

cx0, cy0 = (0.2, 0.2)
cx1, cy1 = (0.2, 0.6)
halfx, halfy = (0.1, 0.1)

poly_coords = [(cx0 - halfx, cy0 - halfy),
               (cx0 + halfx, cy0 - halfy),
               (cx0 + halfx, cy0 + halfy),
               (cx0 - halfx, cy0 + halfy),

               (cx1 - halfx, cy1 - halfy),
               (cx1 + halfx, cy1 - halfy),
               (cx1 + halfx, cy1 + halfy),
               (cx1 - halfx, cy1 + halfy)]


poly = Polygon(poly_coords, color=red, border_color=white,
               border_width=3,  parent=v.scene)

ellipse = Ellipse(border_width=1, border_color=(1,1,1,1), parent=v.scene)

ellipse.center=(0.4, 0.6)
ellipse.radius = (0.1, 0.05)
ellipse.color = (1,1,1,0.1)
# ellipse.border_width = 1
# ellipse.border_color = (1,1,1,1)
ellipse.num_segments = 20
ellipse.start_angle = 0
ellipse.span_angle = 360

rect = Rectangle(center=(0.6, 0.2), width=0.1, height=0.2,
                 color=orange, border_color=white,
                 radius=0.02, parent=v.scene)

regular_poly = RegularPolygon(center=(0.8, 0.2),
                              radius=0.1, sides=6, color=blue,
                              border_color=white, border_width=2,
                              parent=v.scene)
if __name__ == '__main__':
    if sys.flags.interactive != 1:
        app.run()
