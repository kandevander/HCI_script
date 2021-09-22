import matplotlib.pyplot as plt
import os
import numpy as np

q = os.listdir("data")

fig, axes = plt.subplots(2, 3, figsize=(15, 15))

names = {"Adam":  (0, 0), "Andreas": (0, 1), "Asger": (0, 2),
         "Futter": (1, 0), "HH": (1, 1), "Mikkel": (1, 2)}


files = []

for d in q:
    files.append(d)

for f in files:
    names0 = f.split()[0]
    xs = []
    a = f.split(" ")
    b = a[1].split(".")
    first = True
    ystd = []
    with open('data/' + f, "r") as file:
        for line in file.readlines():
            if first:
                first = False
                continue
            line = line.strip()
            x = line.split(',')[0]
            xs.append(float(x))
            ystd.append(np.std(xs))

    ys = []

    for _ in xs:
        ys.append(int(b[0]))
    (x, y) = names[names0]
    axes[x, y].set_title(names0)
    axes[x, y].set_xlabel('score based on distance from center target')
    axes[x, y].set_ylabel('speed of target')
    axes[x, y].errorbar(xs, ys, yerr=ystd, fmt='x')

plt.show()

#plt.savefig('data processing with errorbars.png')



