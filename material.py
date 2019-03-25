#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np

from functools import reduce

allShapes = {
  "rectangle"     : [[1.5,0],   [0,1],           [1.5,1],        [0.75,0.5]],
  "rightKite"     : [[1.0376,0],[0,1.5],         [1.4035,0.9709],[0.6103,0.6177]],
  "hinge"         : [[1.5,0],   [0,0.7],         [1.3594,1.3339],[0.7148,0.5084]],
  "parallelogram" : [[1.5,0],   [0.5172,0.8958], [2.0172,0.8958],[1.0086,0.4479]],
  "kite"          : [[1.0427,0],[-0.3882,1.4488],[1.0557,1.0426],[0.4275,0.6228]],
  "rustedHinge"   : [[1.5,0],   [-0.1021,0.5790],[1.1266,1.4394],[0.6311,0.5046]],
  "isoTrapezoid"  : [[0.7445,0],[-0.3648,1.3617],[1.1351,1.3617],[0.3786,0.6808]],
  "trapezoid"     : [[0.951,0], [0.227,1.2],     [1.727,1.2],    [0.7262,0.6]],
  "random"        : [[0.7,0],   [0.1604,1.1387], [1.6092,1.5269],[0.6174,0.6664]],
  "square"        : [[1.2602,0],[0,1.2602],      [1.2602,1.2602],[0.6301,0.6301]],
  "losange"       : [[1.3,0],   [0.9076,0.9306], [2.2076,0.9306],[1.1038,0.4653]]
}

def rotate(v, theta): # explicit 2D version of a simple rotation matrix
  theta =  theta * (2 * math.pi) / 360;

  return [v[0] * math.cos(theta) - v[1] * math.sin(theta),
          v[0] * math.sin(theta) + v[1] * math.cos(theta)]

def angle2d(v1, v2):
  rounded = round(np.dot(v1,v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)), 15)
  return math.acos(rounded)

def outliers(shape, distance):

  shapesNorm = []

  v1 = shape[0]
  v2 = shape[1]
  v3 = shape[2]
  a = [-v3[0], -v3[1]]
  b = v2 + a
  c = v1 + a
  d = [v1[0]-v2[0],v1[1]-v2[1]]

  shapesNorm.append(np.linalg.norm(v1))
  shapesNorm.append(np.linalg.norm(v2))
  shapesNorm.append(np.linalg.norm(v3))
  shapesNorm.append(np.linalg.norm(b))
  shapesNorm.append(np.linalg.norm(c))
  shapesNorm.append(np.linalg.norm(d))

  mean = sum(shapesNorm) / len(shapesNorm)

  d1 = distance * mean
  d2 = np.linalg.norm(b)

  norb = [((d1/np.linalg.norm(b))*b[0]), ((d1/np.linalg.norm(b))*b[1])]
  o1 = np.array([v3[0] - norb[0],
                  v3[1] - norb[1]])
  o2 = np.array([v3[0] + norb[0],
                 v3[1] + norb[1]])

  alpha = (math.acos(((d1*d1)-(2*d2*d2))/(2*d2*d2))/2)*(360/(2*math.pi))

  o3 = v3 + rotate(norb,alpha)
  o4 = v3 + rotate(norb,-alpha)

  return np.array([o1, o2, o3, o4])

def observed_values(shape):
  v_apbp = shape[0]
  v_bbp  = shape[0] - shape[2]
  v_abp  = shape[0] - shape[1]
  v_apb = shape[2]
  v_aap = - shape[1]
  v_ab = shape[2] - shape[1]
  angle_apbpb = angle2d(shape[0], shape[1])
  angle_aapbp = angle2d(-shape[0], shape[2] - shape[0])
  angle_abbp  = angle2d(shape[1]-shape[2], shape[0] - shape[2])
  angle_apab  = angle2d(-shape[1], shape[2] - shape[1])
  return [v_apbp, v_bbp, v_abp, v_apb, v_aap, v_ab, angle_apbpb, angle_aapbp, angle_abbp, angle_apab]

def pre_compute():
  observable_data = dict()
  for name, points in allShapes.items():
    observable_data[name] = dict()
    points = np.array(points[0:3]).copy()
    outs = outliers(points, 0.3)
    observable_data[name][0] = observed_values(points)
    for i in range(1,5):
      lpoints = points.copy()
      lpoints[0] = outs[i-1]
      observable_data[name][i] = observed_values(lpoints).copy()
  return observable_data

if __name__ == "__main__":
  print(pre_compute()["rectangle"][0])
