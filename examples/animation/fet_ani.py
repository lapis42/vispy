from spiketag.view import scatter_3d_view
from moviepy.editor import VideoClip
from vispy.gloo.util import _screenshot
import numpy as np


fetview = scatter_3d_view()
fetview.size=(500, 500)
x = np.random.randn(10000,3)
x /= x.max()
fetview.show()


def make_frame(i):
    i = int(i*2000)
    fetview.set_data(x[i:i+200, :]*i/2000)
    fetview.transparency = 1
    fetview.on_draw(None) # Update the image on Vispy's canvas
    return _screenshot((0,0,fetview.size[0]*2,fetview.size[1]*2))[:,:,:3]

if __name__ == "__main__":
    # fetview.app.run()
    animation = VideoClip(make_frame, duration=2)
    # animation.write_gif('fet_pop.gif', fps=100)
    animation.write_videofile('fet_pop.mp4', fps=30)
