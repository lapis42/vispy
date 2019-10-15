from moviepy.editor import VideoClip
import numpy as np
from vispy import app, scene
from vispy.gloo.util import _screenshot

canvas = scene.SceneCanvas(keys='interactive')
view = canvas.central_widget.add_view()
view.camera = scene.TurntableCamera(fov=60, up='z', distance=2,
                                    azimuth=30., elevation=65.)

xx, yy = np.arange(-1,1,.02),np.arange(-1,1,.02)
X,Y = np.meshgrid(xx,yy)
R = np.sqrt(X**2+Y**2)
Z = lambda t : 0.1*np.sin(10*R-2*np.pi*t)
surface = scene.visuals.SurfacePlot(x= xx-0.1, y=yy+0.2, z= Z(0),
                        shading='smooth', color=(0.5, 0.5, 1, 1))
view.add(surface)
canvas.show()

# ANIMATE WITH MOVIEPY

def make_frame(t):
    surface.set_data(z = Z(t)) # Update the mathematical surface
    canvas.on_draw(None) # Update the image on Vispy's canvas
    return _screenshot((0,0,canvas.size[0],canvas.size[1]))[:,:,:3]

animation = VideoClip(make_frame, duration=1).resize(width=450)
animation.write_gif('sinc_vispy.gif', fps=30, opt='OptimizePlus')

im = _screenshot((0,0,canvas.size[0],canvas.size[1]))
import matplotlib.pyplot as plt
plt.figure(figsize=(canvas.size[0]/100., canvas.size[1]/100.), dpi=500)
plt.imshow(im, interpolation='none')
plt.show()