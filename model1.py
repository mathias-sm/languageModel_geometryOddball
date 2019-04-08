#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import jnd

def model(set1, set2, parameters):
    """ This model has *no language*. It picks N values, and try to separate
    based on some distance in the resulting space.
    """

    # Unpack the parameters. This may fail if you mess up which model you want
    # to use since they don't have the same number of parameters.
    subject_jnd_l, subject_jnd_a, subject_jnd_d, angle_baseline_a, angle_baseline_d = parameters

    drawned = []
    for i in range(5):
        drawned.append(jnd.draw(set1, subject_jnd_l, subject_jnd_a, subject_jnd_d, angle_baseline_a, angle_baseline_d))
    drawned.append(jnd.draw(set2, subject_jnd_l, subject_jnd_a, subject_jnd_d, angle_baseline_a, angle_baseline_d))

    # For each shape, compute its distance to the mean of all the 5 others
    dist_to_bar = np.empty((6))
    for i in range(6):
        deprived = drawned[:i] + drawned[i+1:]
        b = sum(deprived)/len(deprived)
        dist_to_bar[i] = np.linalg.norm(b - drawned[i])

    # We succeeded if the most distant one was indeed the outlier, the 6th one.
    return np.argmax(dist_to_bar) == 5
