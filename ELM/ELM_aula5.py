import matplotlib.pyplot as plt
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects.lib import ggplot2
R = robjects.r

def main():
    mlbench = importr('mlbench')
    circle = R('mlbench.circle(100)')
    GGplot(circle)


if __name__ == "__main__":
    main()
