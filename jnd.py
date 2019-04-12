#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import material
import numpy as np


def jnd_length(l, s_jnd_l):
    return l*s_jnd_l

def jnd_angle(alpha, s_jnd_a, baseline):
    return s_jnd_a*abs(math.sin(2*alpha) + baseline)


def draw_jnd_length(v, s_jnd_l):
    l = np.linalg.norm(v)
    return np.random.normal(loc=l, scale=jnd_length(l, s_jnd_l))

def draw_jnd_angle(alpha, s_jnd_a, base_a):
    return np.random.normal(alpha, jnd_angle(alpha, s_jnd_a, base_a))

def draw_jnd_direction(v, s_jnd_d, base_d):
    direction = material.angle2d(v, np.array([1,0]))
    return draw_jnd_angle(direction, s_jnd_d, base_d)


def draw_lengths(obs, s_jnd_l):
    """ Returns a noisified version of a shape for the length metric
    """
    return np.array([draw_jnd_length(obs[0], s_jnd_l),
                     draw_jnd_length(obs[1], s_jnd_l),
                     draw_jnd_length(obs[2], s_jnd_l)])

def draw_angles(obs, s_jnd_a, base_a):
    """ Returns a noisified version of a shape for the angle metric
    """
    return np.array([draw_jnd_angle(obs[6], s_jnd_a, base_a),
                     draw_jnd_angle(obs[7], s_jnd_a, base_a),
                     draw_jnd_angle(obs[8], s_jnd_a, base_a)])

def draw_directions(obs, s_jnd_d, base_d):
    """ Returns a noisified version of a shape for the direction metric
    """
    return np.array([draw_jnd_direction(obs[0], s_jnd_d, base_d),
                     draw_jnd_direction(obs[1], s_jnd_d, base_d),
                     draw_jnd_direction(obs[2], s_jnd_d, base_d)])


def corr_list_length(l, s_jnd_l, coeff):
    """ This builds the upper triangular matrix of boolean of similarities
    between all possible length up to jnd modified by a coefficient.
    """
    results = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            # This is debatable: take mu to be the linear mean between the two
            # elements?
            mu = (l[i] + l[j]) / 2
            results.append(int(coeff*abs(l[i] - l[j]) < jnd_length(mu, s_jnd_l)))
    return results


def corr_list_angle(l, s_jnd, base, coeff):
    """ This builds the upper triangular matrix of boolean of similarities
    between all possible angle up to jnd (+ its baseline) modified by a
    coefficient.
    """
    results = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            # This is debatable: take mu to be the linear mean between the two
            # elements?
            mu = (l[i] + l[j]) / 2
            results.append(int(coeff*abs(l[i] - l[j]) < jnd_angle(mu, s_jnd, base)))
    return results
