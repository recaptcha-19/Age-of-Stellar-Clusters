import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import astropy.units as u

class star_cluster:

    def __init__(self, name, DM, mag):
        self.name = name
        self.DM = 0    #distance modulus
        self.mag = np.zeros(5)  #SDSS u, g, r, i, z magnitudes

    def cmd(self):
        #plots a color magnitude diagram for the cluster
        df = pd.read_csv(self.name + ".txt")
        filters = ['u', 'g', 'r', 'i', 'z']
        for i in range(5):
            self.mag[i] = np.array(df[filters[i]])
        u = self.mag[0]
        g = self.mag[1]
        ug = u - g

        plt.scatter(ug, g, s = 5)
        plt.xlabel("$u-g$")
        plt.gca().invert_yaxis()
        plt.ylabel("$g$")
        plt.plot()
        plt.savefig(self.name + "_cmd.png")

        
    

