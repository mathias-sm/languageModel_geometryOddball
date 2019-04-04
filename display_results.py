#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from skopt.plots import plot_objective, plot_evaluations

def show_optimized(optimized):
    print(optimized)
    p1 = plot_objective(optimized)
    p2 = plot_evaluations(optimized)
    plt.set_cmap("viridis")
    plt.grid()
    plt.legend()
    plt.show()

