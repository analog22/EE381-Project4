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
    