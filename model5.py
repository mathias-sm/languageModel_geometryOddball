#!/usr/bin/env python
# -*- coding: utf-8 -*-

import material
import jnd
import numpy as np

def model(set1, set2, parameters):

    # Unpack the parameters. This may fail if you mess up which model you want
    # to use since they don't have the same number of parameters.
    subject_jnd_l, subject_jnd_a, subject_jnd_d, angle_baseline_a, angle_baseline_d, coeff_l, coeff_a , coeff_d = parameters

    # This is "just" model1
    drawned = [[],[],[],[],[],[]]
    # for i in range(5):
        # drawned.append(jnd.draw(set1, subject_jnd_l, subject_jnd_a, subject_jnd_d, angle_baseline_a, angle_baseline_d))
    # drawned.append(jnd.draw(set2, subject_jnd_l, subject_jnd_a, subject_jnd_d, angle_baseline_a, angle_baseline_d))

    # Here comes model2: 
    for i in range(6):

        # Make a deep copy of the shape to not modify in memory the reference
        shape = []
        if (i < 5):
            shape = set1.copy()
        else:
            shape = set2.copy()

        # Computes the matrix
        distances  = jnd.corr_list_length([np.linalg.norm(shape[j]) for j in [0,1,2,3,4,5]], subject_jnd_l, coeff_l)
        # directions = jnd.corr_list_angle([material.angle2d(shape[j], np.array([1,0])) for j in [0,1,2,3,4,5]], subject_jnd_d, angle_baseline_d, coeff_d)
        # angles     = jnd.corr_list_angle([shape[j] for j in [6,7,8,9]], subject_jnd_a, angle_baseline_a, coeff_a)

        # And add it to the output of "model1"
        drawned[i] = np.append(drawned[i], distances)
        # drawned[i] = np.append(drawned[i], directions)
        # drawned[i] = np.append(drawned[i], angles)
        print(distances)

    # For each shape, compute its distance to the mean of all the 5 others
    dist_to_bar = np.empty((6))
    for i in range(6):
        deprived = drawned[:i] + drawned[i+1:]
        b = sum(deprived)/len(deprived)
        dist_to_bar[i] = np.linalg.norm(b - drawned[i])

    # We succeeded if the most distant one was indeed the outlier, the 6th one.
    return np.argmax(dist_to_bar) == 5
