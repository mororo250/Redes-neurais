import math
import numpy
from scipy.interpolate import Rbf

import matplotlib.pyplot as plt
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects.lib import ggplot2
R = robjects.r

kiokioikkkkkk


def pdfnvar(x, m, K, n):
    if (n == 1):
        r = numpy.sqrt(K)
        px = 1/(numpy.sqrt(2*math.pi*r*r)) * numpy.exp(-0.5 * ((x-m)/(r))^2)
    else:
        px = 1/numpy.sqrt((2∗math.pi)**n ∗ (numpy.log((K)))) ∗ numpy.exp(−0.5 ∗ (numpy.transpose(x−m)%∗%(solve(K))%∗%(x−m)))


def treinarRBF(xin, yin, p):


def main():
    mlbench = importr('mlbench')
    circle = R('mlbench.circle(100)')
    print(type(circle))
    print(circle)


if __name__ == "__main__":
    main()
