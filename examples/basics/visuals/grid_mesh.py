"""
Demonstration of a mesh constructed in a grid about x,y,z coordinates.
"""

from vispy import scene
import numpy as np
from scipy.special import sph_harm


from vispy.io.mesh import read_mesh

canvas = scene.SceneCanvas(keys='interactive')
view = canvas.central_widget.add_view()

(vertices, faces, vertex_colors, _) = read_mesh('/Users/laic/Downloads/tri_cl.obj')
# color = np.zeros((ys.shape[0], 4)) * np.array([0,1,1,1])
vertex_colors[:,1] += 1
vertex_colors[:,2] = 0
mesh = scene.visuals.Mesh(vertices, faces, vertex_colors)
# mesh.ambient_light_color = vispy.color.Color('white')
view.add(mesh)

view.camera = 'turntable'
canvas.show()

if __name__ == '__main__':
    canvas.app.run()
