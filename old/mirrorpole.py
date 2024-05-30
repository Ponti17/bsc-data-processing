import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from _handledata import DataHandler
from _plot import Plot

reader = DataHandler()
mos = Plot()

reader.load("pch")

id = 1.12e-6
gateL = "10"
vdsrc = "0.3"
fp = 1.2e3 * 1000
mos.setgateL(gateL)
mos.setvdsrc(vdsrc)
gmid_arr    = reader.get_axis("gmoverid", mos.getvdsrc(), mos.getgateL())
ft_arr      = reader.get_axis("ft", mos.getvdsrc(), mos.getgateL())
idw_arr     = reader.get_axis("id/w", mos.getvdsrc(), mos.getgateL())

print("gmid_arr: ", gmid_arr)

vals = {
    "gmid": [],
    "pole": [],
    "w": []
}
for gmid in range(5, 26):
    gm = gmid * id
    for i in range(0, len(gmid_arr)):
        if gmid_arr[i] < gmid:
            gmid_true = gmid_arr[i]
            ft = ft_arr[i]
            idw = idw_arr[i]
            break
    cgg = 2*(gm / (2*np.pi*ft))
    pole = gm / (2*np.pi*cgg)
    w = id / idw
    vals["gmid"].append(gmid_true)
    vals["pole"].append("{:.2e}".format(float(pole)))
    vals["w"].append("{:.2e}".format(float(w)))

for j in vals["pole"]:
    if float(j) > fp:
        gmid = vals["gmid"][vals["pole"].index(j)]
        pole = j
        w = vals["w"][vals["pole"].index(j)]
        WL = float(w) * gateL
        print("gmid: {0}, pole: {1}, w: {2}, WL: {3}".format(gmid, pole, w, WL))
        