import numpy as np
import matplotlib.pyplot as plt
from star_cluster import star_cluster
import pandas as pd

def dm_estimator(name):
    #plots a color magnitude diagram for the cluster and a plot to manually find the distance modulus
    sc = star_cluster(name)
    df = pd.read_csv(name + ".csv")
    del df['objid']
    del df['ra']
    del df['dec']
    sc.mag = df.to_numpy()
    sc.mag = np.transpose(sc.mag)
    u = sc.mag[0]
    g = sc.mag[1]
    r = sc.mag[2]
    i = sc.mag[3]
    z = sc.mag[4]
    ug = u - g
    gr = g - r
    ri = r - i
    iz = i - z
    plt.scatter(ug, g, s = 5)
    plt.xlabel("$g-r$")
    plt.gca().invert_yaxis()
    plt.ylabel("$r$")
    plt.title("Color Magnitude Diagram of " + name)
    plt.show()
    plt.savefig(name + "_cmd.png")

    
    iso_path = name + "_iso0.2.txt"
    iso = np.loadtxt(iso_path, skiprows = 9)
    iso = np.transpose(iso)
    u_iso = iso[5]
    g_iso = iso[6]
    r_iso = iso[7]
    i_iso = iso[8]
    z_iso = iso[9]
    ug_iso = u_iso - g_iso
    gr_iso = g_iso - r_iso
    ri_iso = r_iso - i_iso
    iz_iso = i_iso - z_iso
    plt.scatter(ug, g, s = 5)
    plt.plot(ug_iso, g_iso, c = 'r')
    plt.gca().invert_yaxis()
    plt.show()

clusters = ["ngc_2419", "ngc_4147", "ngc_5053", "ngc_6341", "ngc_7006", "ngc_7089"]
for cluster in clusters:
    dm_estimator(cluster)
    