import matplotlib.pyplot as plt
import numpy as np
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

x = np.linspace(-2, 2, 200)
duration = 2

fig, ax = plt.subplots(2,1)
def make_frame(t):
    ax[0].clear()
    ax[0].plot(x, np.sinc(x**2) + np.sin(x + 2*np.pi/duration * t), lw=3)
    ax[0].set_ylim(-1.5, 2.5)
    ax[1].clear()
    ax[1].plot(x, np.sin(x**2) + np.sin(x + 2*np.pi/duration * t), lw=3, c='r')
    ax[1].set_ylim(-1.5, 2.5)
    return mplfig_to_npimage(fig)

animation = VideoClip(make_frame, duration=duration)
animation.write_videofile('matplotlib.mp4', fps=20)