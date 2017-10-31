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
    
    nbins = 100
    # Create bins and histogram
    bins = [float(x) for x in np.linspace(min(T), max(T), nbins)]
    h1, bin_edges = np.histogram(T, bins, density=True)
    # Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0]    # width of bars in the bargraph
    # close('all')
    #
    fig1 = plt.figure(1)
    plt.bar(b1, h1, width=barwidth, edgecolor='w')
    
    
    fx = 2 * np.exp(-2*bin_edges)
    plt.plot(bins, fx, color='r')
    
    plt.title('PDF of exponentially distributed random variables and comparison with function')
    plt.xlabel('x')
    plt.ylabel('PDF f(x)')