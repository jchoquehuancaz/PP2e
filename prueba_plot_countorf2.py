#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 15:14:34 2017

@author: jj-pc
"""


import numpy as np
from functions_mlem import predict_label
import matplotlib.pyplot as plt

r_grid = np.linspace(-2,2,100)
x1_grid,x2_grid = np.meshgrid(r_grid,r_grid)
n_x1,n_x2 = x1_grid.shape

N_points = n_x1*n_x2

x0 = np.ones((1,N_points))
x1 = np.reshape(x1_grid,(1,N_points))
x2 = np.reshape(x2_grid,(1,N_points))

x_grid = np.concatenate((x1,x2,x0),axis=0)

y_est_grid = predict_label(W,x_grid)
d_est_grid = np.argmax(y_est_grid ,axis=0)
D_est_grid = np.reshape(d_est_grid,(n_x1,n_x2))

plt.figure(10)

plt.plot(X_tr[0, idx_tr1], X_tr[1, idx_tr1], '.b')
plt.plot(X_tr[0, idx_tr2], X_tr[1, idx_tr2], '*r')
plt.plot(X_tr[0, idx_tr3], X_tr[1, idx_tr3], 'og')

idx_d0 = d_est_grid==0
idx_d1 = d_est_grid==1
idx_d2 = d_est_grid==2

plt.plot(x_grid[0, idx_d0], x_grid[1, idx_d0], '.b')
plt.plot(x_grid[0, idx_d1], x_grid[1, idx_d1], '.r')
plt.plot(x_grid[0, idx_d2], x_grid[1, idx_d2], '.g')



