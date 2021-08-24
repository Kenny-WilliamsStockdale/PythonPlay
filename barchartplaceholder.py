import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')

"""
Demonstrates one way of embedding Matplotlib figures into a PySimpleGUI window.
Basic steps are:
 * Create a Canvas Element
 * Layout form
 * Display form (NON BLOCKING)
 * Draw plots onto convas
 * Display form (BLOCKING)
 
"""

def DES1():
# ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE -------------------------------
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]

    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    t = np.arange(len(labels))
    fig, ax = plt.subplots()
    width = 0.35
    rects1 = ax.bar(t - width/2, men_means, width, label='Men')
    rects2 = ax.bar(t + width/2, women_means, width, label='Women')

    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(t)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    # ------------------------------- END OF YOUR MATPLOTLIB CODE -------------------------------

    # ------------------------------- Beginning of Matplotlib helper code -----------------------

    def draw_figure(canvas, figure):
            figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
            figure_canvas_agg.draw()
            figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
            return figure_canvas_agg

    # ------------------------------- Beginning of GUI CODE -------------------------------

    # define the window layout
    layout = [[sg.Canvas(key='-CANVAS-')],
            [sg.Button('ZOOM +'), sg.Button('ZOOM -')],
            [sg.Multiline(default_text='Data Information Summary:', size=(35, 5)), sg.Multiline(default_text='Chat System:',size=(35, 5))],
            [sg.Button('Previous'), sg.Button('Next')],
            [sg.Button('Back'), sg.Button('Logout')]]

    # create the form and show it without the plot
    window = sg.Window('Demo Application', layout, finalize=True, element_justification='center', size=(800, 700))

    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    event, values = window.read()

    window.close()
DES1()