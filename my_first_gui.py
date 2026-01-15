# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 16:38:41 2026

@author: lauwy
"""

#%% S1 - LIB
import tkinter as tk 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#%% S2 - Initial values

#%% S3 - Gui Callback

#%% S4 - Create model

#%% S5 - Create GUI Elements
root = tk.Tk()
root.geometry("1000x750")
root.resizable(False, False)
root.title('My First GUI')

figure1 = plt.Figure(figsize=(4,4), dpi=150)
canvas = FigureCanvasTkAgg(figure1, master=root)
canvas_widget = canvas.get_tk_widget()
#%% S6 - Place GUI Elements
canvas_widget.pack(side="right", fill="y")

#%% S7- Create event loop
root.mainloop()