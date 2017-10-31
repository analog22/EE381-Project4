# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:10:24 2017

@author: Matthew
Project 4, Problem 1

x1, x2, ... xn are RV
the sum Sn = x1 + x2 + ... xn is a new RV
will have a distribution close to normal (or gaussian) as n gets larger

"""

import numpy as np
from matplotlib import pyplot as plt

def CentralLimitTheorem(N) :
    n = 15
    S = []
    # X is the array with the values of the RV to be plotted
    a = 1; b = 3;           # a = min bookwidth; b = max bookwidth
    nbooks = n; nbins = 30; # number of books; number of bins
    edgecolor='w';          # color separating bars in bargraph
    #
    for k in range(N) :
        x = np.random.uniform(1,3,n)
        S.append(sum(x))
    
    # Create bins and histogram
    bins = [float(x) for x in np.linspace(nbooks*a, nbooks*b, nbins+1)]
    h1, bin_edges = np.histogram(S, bins, density=True)
    # Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges)-1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1+be2)/2
    barwidth = b1[1]-b1[0]    # width of bars in the bargraph
    # close('all')
    #
    fig1 = plt.figure(1)
    plt.bar(b1, h1, width=barwidth, edgecolor=edgecolor)
    
    mu = 2 * n
    sigma = 0.57 * np.sqrt(n)
    fx1 = 1/(sigma * np.sqrt(2 * np.pi))
    fx2 = np.exp(-((bin_edges-mu)**2)/(2*((sigma)**2)))
    fx = fx1 * fx2
    plt.plot(bins, fx, color='r')
    
    plt.title('PDF of book stack height and comparison with Gaussian')
    plt.xlabel('Book stack height for n=' +str(n) + ' books')
    plt.ylabel('PDF')