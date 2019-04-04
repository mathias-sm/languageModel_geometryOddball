#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A file to simulate the two models Stan and I have
"""

import material
import jnd
import math
import numpy as np
import model1

def model(set1, set2, subject_jnd):
    base = []
    for i in range(5):
        drawned = jnd.draw(set1, subject_jnd).copy()
        base.append(drawned)
    drawned = jnd.draw(set2, subject_jnd).copy()
    base.append(drawned)

    for i in range(6):
        shape = []
        if (i < 5):
            shape = set1.copy()
        else:
            shape = set2.copy()
        angles = jnd.corr_list_angle([shape[j] for j in [6,7,8,9]], subject_jnd)
        distances = jnd.corr_list_length([np.linalg.norm(shape[j]) for j in [0,1,2,3,4,5]], subject_jnd)
        directions = jnd.corr_list_angle([material.angle2d(shape[j], np.array([1,0])) for j in [0,1,2,3,4,5]], subject_jnd)
        np.append(base[i], angles)
        np.append(base[i], distances)
        np.append(base[i], directions)

    dist_to_bar = np.empty((6))
    for i in range(6):
        deprived = base[:i] + base[i+1:]
        b = sum(deprived)/len(deprived)
        no_l_deprived = base[:i] + base[i+1:]
        v1 = (b - base[i])
        dist_to_bar[i] = np.linalg.norm(b - drawned[i])

    return np.argmax(dist_to_bar) == 5
