#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A file to simulate the two models Stan and I have
"""

import numpy as np
import jnd

# This model has *no language*. It picks N values, and try to separate again.
def model(set1, set2, subject_jnd_l, subject_jnd_a, subject_jnd_d, angle_baseline_a, angle_baseline_d):
    drawned = []
    for i in range(5):
        drawned.append(jnd.draw(set1, subject_jnd_l, subject_jnd_a, subject_jnd_d, angle_baseline_a, angle_baseline_d))
    drawned.append(jnd.draw(set2, subject_jnd_l, subject_jnd_a, subject_jnd_d, angle_baseline_a, angle_baseline_d))

    dist_to_bar = np.empty((6))
    for i in range(6):
        deprived = drawned[:i] + drawned[i+1:]
        b = sum(deprived)/len(deprived)
        dist_to_bar[i] = np.linalg.norm(b - drawned[i])

    return np.argmax(dist_to_bar) == 5
