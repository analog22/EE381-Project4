# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 08:58:22 2017

@author: Matthew
Project 4, Problem 3

Craete 24 exponential rv
x1, x2, ... x24
with beta = 45
each rv represents a battery with average lifetime beta = 45 days
lifetime of a battery is exponential rv with beta = 45
the sum of 24 rv will be approx normal
24 rv represents the lifetime of a carton of batteries

Generate 24 exponenetial rv
x1, x2, ... x24
sum s = x1 + x2 + ... + x24
do a histogram of S
compare to normal
generate the CDF of S
use "cumsum" function
H1 = cumsum(h1) * barwidth
"""

import numpy as np
from matplotlib import pyplot as plt

def SumRV(N) :
    beta = 45
    C = []
    for k in range(N) :
        T = np.random.exponential(beta, 24)
        C.append(sum(T))
    
    nbins=100
    # Create bins and histogram
    bins = [float(x) for x in np.linspace(min(C), max(C), nbins)]
    h1, bin_edges = np.histogram(C, bins, density=True)
    # Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0]    # width of bars in the bargraph
    # close('all')
    #
    fig1 = plt.figure(1)
    plt.bar(b1, h1, width=barwidth, edgecolor='w')
    
    mu = 24 * beta
    sigma = beta * np.sqrt(24)
    fx1 = 1/(sigma * np.sqrt(2 * np.pi))
    fx2 = np.exp(-((bin_edges-mu)**2)/(2*((sigma)**2)))
    fx = fx1 * fx2
    plt.plot(bins, fx, color='r')
    
    plt.title('PDF of sum of random variables and comparison with normal distribution')
    plt.xlabel('Days')
    plt.ylabel('Probability of lifetime')
    
    fig2 = plt.figure(2)
    H1 = np.cumsum(h1) * barwidth
    plt.bar(b1, H1, width=barwidth, edgecolor='w')
    
    plt.title('CDF plot of the lifetime of one carton')
    plt.xlabel('Days')
    plt.ylabel('Probability of lifetime')