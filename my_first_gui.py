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
# Window creation
root = tk.Tk()
root.geometry("1000x750")
root.resizable(False, False)
root.title('My First GUI')

#Subwindow creation
figure1 = plt.Figure(figsize=(4,4), dpi=150)
canvas = FigureCanvasTkAgg(figure1, master=root)
canvas_widget = canvas.get_tk_widget()

# Slider
slider = tk.Scale(master=root, from_=10,to=180,label="Joint angle",resolution=1,length=200,orient='horizontal')
#%% S6 - Place GUI Elements
# Subvenster
canvas_widget.pack(side="right", fill="y")

# Slider
slider.pack(side="bottom", pady=100)
#%% S7- Create event loop
root.mainloop()