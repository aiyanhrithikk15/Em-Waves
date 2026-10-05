import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button

# Wave parameters
x = np.linspace(0, 4 * np.pi, 600)

# Current values
a = 1.0
f = 1.0
lam = 2.0
phase = 0.0
direction = 1

fig, ax = plt.subplots(figsize=(10, 5))
plt.subplots_adjust(left=0.08, right=0.97, bottom=0.32)

ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-1.8, 1.8)
ax.set_xlabel("Distance x (m)")
ax.set_ylabel("Field amplitude (V/m)")
ax.set_title("Electromagnetic Wave Simulation")
ax.grid(True, alpha=0.3)

line_E, = ax.plot([], [], color="tab:blue", lw=2.5, label="Electric field E")
line_B, = ax.plot([], [], color="tab:orange", lw=2, label="Magnetic field B")
ax.legend(loc="upper right")
phase_readout = ax.text(0.02, 0.95, "", transform=ax.transAxes, va="top")

# Sliders
ax_amp = plt.axes([0.18, 0.22, 0.52, 0.03])
ax_freq = plt.axes([0.18, 0.16, 0.52, 0.03])
ax_wave = plt.axes([0.18, 0.10, 0.52, 0.03])
ax_phase = plt.axes([0.18, 0.28, 0.52, 0.03])

slider_amp = Slider(ax_amp, "Amplitude (V/m)", 0.2, 2.0, valinit=1.0)
slider_freq = Slider(ax_freq, "Frequency (Hz)", 0.2, 3.0, valinit=1.0)
slider_wave = Slider(ax_wave, "Wavelength (m)", 0.5, 6.0, valinit=2.0)
slider_phase = Slider(ax_phase, "Phase (rad)", 0.0, 2 * np.pi, valinit=0.0)

# Direction toggle button
ax_dir = plt.axes([0.76, 0.12, 0.18, 0.10])
dir_button = Button(ax_dir, "Toggle\ndirection")

current_frame = 0


def update(frame):
    global a, f, lam, phase, direction, current_frame
    current_frame = frame
    t = frame / 20
    k = 2 * np.pi / lam
    omega = 2 * np.pi * f
    E = direction * a * np.sin(k * x - omega * t + phase)
    B = 0.8 * a * np.sin(k * x - omega * t + phase)
    line_E.set_data(x, E)
    line_B.set_data(x, B)
    phase_readout.set_text(f"Phase offset: {phase:.2f} rad ({np.degrees(phase):.0f} deg)")
    return line_E, line_B


def on_amp_change(val):
    global a
    a = slider_amp.val
    fig.canvas.draw_idle()


def on_freq_change(val):
    global f
    f = slider_freq.val
    fig.canvas.draw_idle()


def on_wave_change(val):
    global lam
    lam = slider_wave.val
    fig.canvas.draw_idle()


def on_phase_change(val):
    global phase
    phase = slider_phase.val
    update(current_frame)
    fig.canvas.draw_idle()


def toggle_direction(_):
    global direction
    direction *= -1
    fig.canvas.draw_idle()


slider_amp.on_changed(on_amp_change)
slider_freq.on_changed(on_freq_change)
slider_wave.on_changed(on_wave_change)
slider_phase.on_changed(on_phase_change)
dir_button.on_clicked(toggle_direction)

anim = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=40, blit=False)
plt.show()
