import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

path = r'd:\First Year\Applied Physics\Em wave simulator\em_wave.ipynb'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
print('cells=', len(data.get('cells', [])))

x = np.linspace(0, 4 * np.pi, 600)

def display_wave(amplitude=1.0, frequency=1.0, wavelength=2.0, phase=0.0, direction=1):
    k = 2 * np.pi / wavelength
    omega = 2 * np.pi * frequency
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 4 * np.pi)
    ax.set_ylim(-1.8 * amplitude, 1.8 * amplitude)
    ax.set_xlabel('Distance x')
    ax.set_ylabel('Field amplitude')
    ax.set_title('Electromagnetic Wave Simulation')
    ax.grid(True, alpha=0.3)
    line_E, = ax.plot([], [], color='tab:blue', lw=2.5, label='Electric field E')
    line_B, = ax.plot([], [], color='tab:orange', lw=2, label='Magnetic field B')
    ax.legend(loc='upper right')

    def update(frame):
        t = frame / 20
        E = direction * amplitude * np.sin(k * x - omega * t + phase)
        B = 0.8 * amplitude * np.sin(k * x - omega * t + phase)
        line_E.set_data(x, E)
        line_B.set_data(x, B)
        return line_E, line_B

    anim = FuncAnimation(fig, update, frames=np.arange(0, 100), blit=True, interval=40)
    plt.close(fig)
    return HTML(anim.to_jshtml())

html = display_wave()
print(type(html).__name__)
print('interactive_ok')
