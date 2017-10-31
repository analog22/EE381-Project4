#-*- coding: utf-8 -*-
"""
Created on Wed Oct 25 08:56:38 2017

@author: Matthew
Project 4, Problem 2

problem 2
plot exponential RV
PDF 2e^(-2x)
python
x = exponential(beta) > (1/beta)e^(-(1/beta)^x)
simulate exponential rv with beta = 0.5
f(x) = 2e^(-2x)
compare with function

"""

import numpy as np
from matplotlib import pyplot as plt

def ExponentialRV(N):
    beta = 0.5
    T = np.random.exponential(beta, N)
    
    # Create bins and histogram
    bins = [float(x) for x in np.linspace(min(T), max(T), N+1)]
    h1, bin_edges = np.histogram(T, bins, density=True)
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0]    # width of bars in the bargraph
    # close('all')
    #
    
    #plt.bar(b1, h1, width=barwidth, edgecolor='w')
    plt.hist(T, width=barwidth, edgecolor='w')