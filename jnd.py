
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import material
import numpy as np

def jnd_length(l, subject_jnd_l):
    return l*subject_jnd_l

def jnd_angle(alpha, subject_jnd_a, baseline):
    # FIX THESE PARAMETERS
    return subject_jnd_a*abs(math.sin(2*alpha) + baseline)

def draw_jnd_length(v, subject_jnd_l):
    l = np.linalg.norm(v)
    return np.random.normal(loc=l, scale=l*subject_jnd_l)

def draw_jnd_angle(alpha, subject_jnd_a, angle_baseline_a):
    return np.random.normal(alpha, jnd_angle(alpha, subject_jnd_a, angle_baseline_a))

def draw_jnd_direction(v, subject_jnd_d, angle_baseline_d):
    # This feels too crude. Maybe there are special cases for horizontal and
    # vertical alignments.
    # Cardinal rules: Visual orientation perception reflects knowledge of
    # environmental statistics Ahna R. Girshick,1,2 Michael S. Landy,1,2 and Eero
    # P. Simoncelli1,2,3,4
    direction = material.angle2d(v, np.array([1,0]))
    return draw_jnd_angle(direction, subject_jnd_d, angle_baseline_d)

def draw(obs, subject_jnd_l, subject_jnd_a, subject_jnd_d, angle_baseline_a, angle_baseline_d):
    return np.array([draw_jnd_length(obs[0], subject_jnd_l),
                    draw_jnd_length(obs[1], subject_jnd_l),
                    draw_jnd_length(obs[2], subject_jnd_l),
                    draw_jnd_angle(obs[6], subject_jnd_a, angle_baseline_a),
                    draw_jnd_angle(obs[7], subject_jnd_a, angle_baseline_a),
                    draw_jnd_angle(obs[8], subject_jnd_a, angle_baseline_a),
                    draw_jnd_direction(obs[0], subject_jnd_d, angle_baseline_d),
                    draw_jnd_direction(obs[1], subject_jnd_d, angle_baseline_d),
                    draw_jnd_direction(obs[2], subject_jnd_d, angle_baseline_d),
    ])

def corr_list_angle(l, subject_jnd):
    results = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            mu = (l[i] + l[j]) / 2
        if abs(l[i] - l[j]) < jnd_angle(mu, subject_jnd):
            results.append(1)
        else:
            results.append(0)
    return results

def corr_list_length(l, subject_jnd):
    results = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            mu = (l[i] + l[j]) / 2
        if abs(l[i] - l[j]) < jnd_length(mu, subject_jnd):
            results.append(1)
        else:
            results.append(0)
    return results
