import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0, 4 * np.pi, 80)
z = np.linspace(0, 4 * np.pi, 80)
X, Z = np.meshgrid(x, z)

def display_wave(amplitude=1.0, frequency=1.0, wavelength=2.0, phase=0.0, direction=1):
    k = 2 * np.pi / wavelength
    omega = 2 * np.pi * frequency
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(0, 4 * np.pi)
    ax.set_ylim(0, 4 * np.pi)
    ax.set_zlim(-1.8 * amplitude, 1.8 * amplitude)
    ax.set_xlabel('x')
    ax.set_ylabel('z')
    ax.set_zlabel('Field')
    ax.set_title('3D Electromagnetic Wave Model')
    ax.view_init(elev=28, azim=35)

    def update(frame):
        ax.clear()
        ax.set_xlim(0, 4 * np.pi)
        ax.set_ylim(0, 4 * np.pi)
        ax.set_zlim(-1.8 * amplitude, 1.8 * amplitude)
        ax.set_xlabel('x')
        ax.set_ylabel('z')
        ax.set_zlabel('Field')
        ax.set_title('3D Electromagnetic Wave Model')
        ax.view_init(elev=28, azim=35 + frame * 0.5)
        t = frame / 20
        E = direction * amplitude * np.sin(k * X - omega * t + phase)
        B = 0.8 * amplitude * np.sin(k * X - omega * t + phase)
        ax.plot_surface(X, Z, E, cmap='viridis', alpha=0.9, linewidth=0)
        ax.plot_surface(X, Z, B, cmap='plasma', alpha=0.35, linewidth=0)

    anim = FuncAnimation(fig, update, frames=np.arange(0, 20), interval=50, blit=False)
    plt.close(fig)
    return HTML(anim.to_jshtml())

html = display_wave()
print(type(html).__name__)
print('3d_wave_ok')
