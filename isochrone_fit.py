import numpy as np
import matplotlib.pyplot as plt
from star_cluster import star_cluster
import pandas as pd

ngc_2419 = star_cluster("ngc_2419")
ngc_4147 = star_cluster("ngc_4147")
ngc_5053 = star_cluster("ngc_5053")
ngc_6341 = star_cluster("ngc_6341")
ngc_7006 = star_cluster("ngc_7006")
ngc_7089 = star_cluster("ngc_7089")

#approximate distance moduli obtained manually based on visual cues
ngc_2419.DM = 14.5
ngc_4147.DM = 14.5
ngc_5053.DM = 14.5
ngc_6341.DM = 14.5
ngc_7006.DM = 14.5
ngc_7089.DM = 14.5

star_clusters = [ngc_2419, ngc_4147, ngc_5053, ngc_6341, ngc_7006, ngc_7089]
ages = np.array([2, 5, 8, 11])

for cluster in star_clusters:
    df = pd.read_csv(cluster.name + ".csv")
    del df['objid']
    del df['ra']
    del df['dec']
    cluster.mag = df.to_numpy()
    cluster.mag = np.transpose(cluster.mag)
    u = cluster.mag[0]
    g = cluster.mag[1]
    ug = u - g
    plt.scatter(ug, g - cluster.DM, s = 5)
    plt.gca().invert_yaxis()
    for age in ages:
        iso_path = cluster.name + "_iso{}.txt".format(int(age))
        iso = np.loadtxt(iso_path, skiprows = 9)
        iso = np.transpose(iso)
        u_iso = iso[5]
        g_iso = iso[6]
        ug_iso = u_iso - g_iso
        plt.plot(ug_iso, g_iso, label = "{} Gyr".format(age))
    plt.xlabel("$u - g$")
    plt.ylabel("g")
    plt.title("Isochrone fit of" + cluster.name)
    plt.legend()
    plt.show()
    plt.savefig(cluster.name + "_iso_fit.png")
        