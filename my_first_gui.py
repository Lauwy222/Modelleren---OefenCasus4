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

#%% S2 - Initial values / constanten
initial_elbow_ang = 60
rad_to_deg = np.pi / 180

fore_arm = 40      # lengte onderarm
ins_dist = 4       # insertieafstand vanaf elleboog (cm)
origo_y = 30       # origo op bovenarm: 30 cm boven elleboog

#%% S3 - Gui Callback
def slider_changed(*_):
    calculate_model()

#%% S4 - Create model
def calculate_model():
    # vaste punten
    elbow = [0, 0]
    shoulder = [0, 40]
    origo = [0, origo_y]   # op bovenarm

    # actuele hoek
    elbow_ang = slider.get()
    segment_ang = 90 - elbow_ang

    # hand (einde onderarm)
    dist_x_hand = np.cos(segment_ang * rad_to_deg) * fore_arm
    dist_y_hand = np.sin(segment_ang * rad_to_deg) * fore_arm
    hand = [elbow[0] + dist_x_hand, elbow[1] + dist_y_hand]

    # insertiepunt spier (op onderarm, 4 cm vanaf elleboog)
    dist_x_ins = np.cos(segment_ang * rad_to_deg) * ins_dist
    dist_y_ins = np.sin(segment_ang * rad_to_deg) * ins_dist
    insertion = [elbow[0] + dist_x_ins, elbow[1] + dist_y_ins]

    # spierlengte (pythagoras)
    musc_vect = [origo[0] - insertion[0], origo[1] - insertion[1]]
    musc_length = np.sqrt(musc_vect[0]**2 + musc_vect[1]**2)
    musc_length = round(musc_length, 2)

    # update label
    muscval_lbl.config(text=musc_length)

    # plot
    figure1.clear()
    ax1 = figure1.add_subplot()

    # bovenarm
    ax1.plot([shoulder[0], elbow[0]], [shoulder[1], elbow[1]], color="blue")
    # onderarm
    ax1.plot([elbow[0], hand[0]], [elbow[1], hand[1]], color="blue")
    # spier
    ax1.plot([origo[0], insertion[0]], [origo[1], insertion[1]], color="red")

    ax1.set(xlim=(-10, 60), ylim=(-60, 60))
    ax1.set_aspect('equal')
    canvas.draw()

#%% S5 - Create GUI Elements
root = tk.Tk()
root.geometry("1000x750")
root.resizable(False, False)
root.title('My First GUI')

# Plot in tkinter
figure1 = plt.Figure(figsize=(4, 4), dpi=150, facecolor="#d9d9d9")
canvas = FigureCanvasTkAgg(figure1, master=root)
canvas_widget = canvas.get_tk_widget()

# Logo (zorg dat btlogo.png in dezelfde map staat)
pict = tk.PhotoImage(file="asset/btlogo.png")
pict_lbl = tk.Label(master=root, image=pict)

# Labels (spierlengte)
musc_lbl = tk.Label(master=root, text="Muscle length")
muscval_lbl = tk.Label(master=root, text="", bg="white", width=10)

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

#%% S6 - Place GUI Elements
canvas_widget.pack(side="right", fill="y")

# links (volgorde = van boven naar beneden)
pict_lbl.pack(side="top", pady=100)
musc_lbl.pack(side="top", pady=(10, 5))
muscval_lbl.pack(side="top", pady=(0, 40))
slider.pack(side="bottom", pady=100)

# start-tekening
calculate_model()

#%% S7 - Create event loop
root.mainloop()
