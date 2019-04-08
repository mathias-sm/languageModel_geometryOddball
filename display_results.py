#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import matplotlib.pyplot as plt
from skopt.plots import plot_objective, plot_evaluations

def show_optimized(optimized, output=None):
    """ Takes the dump of an optimizer and outputs relevant infos

    Both with visualisations, in the terminal and in the optional output file
    where it puts the best parameters in a JSON format
    """
    print(optimized)
    if output != None:
        x = optimized.x
        data = dict()
        data["jnd_length"]       = x[0]
        data["jnd_angle"]        = x[1]
        data["jnd_direction"]    = x[2]
        data["angle_baseline_a"] = x[3]
        data["angle_baseline_d"] = x[4]
        if len(x) > 5:
            data["coef_l"]       = x[5]
            data["coef_a"]       = x[6]
            data["coef_d"]       = x[7]
        else:
            data["coef_l"]       = 1.
            data["coef_a"]       = 1.
            data["coef_d"]       = 1.
        json.dump(data, open(output, "w"), indent=4)
    p1 = plot_objective(optimized)
    p2 = plot_evaluations(optimized)
    plt.set_cmap("viridis")
    plt.grid()
    plt.legend()
    plt.show()

