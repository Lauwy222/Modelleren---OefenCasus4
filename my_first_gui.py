# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 16:38:41 2026

@author: lauwy
"""

#%% S1 - LIB
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

#%% S2 - Initial values
initial_elbow_ang = 60
rad_to_deg = np.pi / 180

#%% S3 - Gui Callback
def slider_changed(*_):
    # bij elke sliderbeweging model opnieuw tekenen
    calculate_model()

#%% S4 - Create model
def calculate_model():
    # vaste punten / lengtes
    elbow = [0, 0]
    shoulder = [0, 40]
    fore_arm = 40

    # actuele hoek uit slider
    elbow_ang = slider.get()
    segment_ang = 90 - elbow_ang

    # bereken handpositie met sin/cos
    dist_x = np.cos(segment_ang * rad_to_deg) * fore_arm
    dist_y = np.sin(segment_ang * rad_to_deg) * fore_arm
    hand = [elbow[0] + dist_x, elbow[1] + dist_y]

    # plot
    figure1.clear()
    ax1 = figure1.add_subplot()

    # bovenarm: shoulder -> elbow
    ax1.plot([shoulder[0], elbow[0]], [shoulder[1], elbow[1]], color="blue")

    # onderarm: elbow -> hand
    ax1.plot([elbow[0], hand[0]], [elbow[1], hand[1]], color="blue")

    ax1.set(xlim=(-10, 60), ylim=(-60, 60))
    ax1.set_aspect('equal')

    canvas.draw()

#%% S5 - Create GUI Elements
# Window creation
root = tk.Tk()
root.geometry("1000x750")
root.resizable(False, False)
root.title('My First GUI')

# Subwindow creation (matplotlib in tkinter)
figure1 = plt.Figure(figsize=(4, 4), dpi=150, facecolor='#F0F0F0')
canvas = FigureCanvasTkAgg(figure1, master=root)
canvas_widget = canvas.get_tk_widget()

# Slider
slider = tk.Scale(
    master=root,
    from_=10, to=180,
    label="Joint angle",
    resolution=1,
    length=200,
    command=slider_changed,
    orient='horizontal'
)
slider.set(initial_elbow_ang)

# teken direct 1e keer (startpositie)
calculate_model()

#%% S6 - Place GUI Elements
canvas_widget.pack(side="right", fill="y")
slider.pack(side="bottom", pady=100)

#%% S7 - Create event loop
root.mainloop()
