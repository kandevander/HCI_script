import matplotlib.pyplot as plt
import os
import numpy as np


def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

q = os.listdir("data")

fig, axes = plt.subplots(2, 2, figsize=(15, 15))

reaction_time = {'2': (0, 0), '5': (0, 1),
                 '10': (1, 0), '15': (1, 1)}

files = []

xs = []

ys = []

for d in q:
    files.append(d)

for f in files:
    names0 = f.split()[0]
    a = f.split(" ")
    b = a[1].split(".")
    first = True
    with open('data/' + f, "r") as file:
        for line in file.readlines():
            if first:
                first = False
                continue
            line = line.strip()
            x = line.split(',')[0]
            xs.append(float(b[0]))
            ys.append(float(x))
data = {2: [], 5: [], 10: [], 15: []}

for(x, y) in zip(xs, ys):
    data[x].append(y)

for idx, key in enumerate(data):
    ax = axes[idx // 2][idx % 2]
    data_points = data[key]

    ystd = np.std(data_points)

    ymean = np.mean(data_points)

    ymin = min(data_points)

    ymax = max(data_points)

    range_length = ymax - ymin

    range_min = ymin - range_length * 0.05

    range_max = ymax + range_length * 0.05

    y_new = np.linspace(range_min, range_max, 100)

    z = gaussian(y_new, ymean, ystd)

    ax.plot(y_new, z)

    ys2 = []

    for _ in data_points:
        ys2.append(0)

    ax.scatter(data_points, ys2)
    ax.set_xlabel('score based on distance from center target', size=15)
    ax.set_ylabel('score based on distance from center target', size=15)

axes[0, 0].set_title('Speed 2', size=25)
axes[0, 1].set_title('speed 5', size=25)
axes[1, 0].set_title('Speed 10', size=25)
axes[1, 1].set_title('Speed 15', size=25)
plt.show()

#plt.savefig('data processing with gaussian distribution.png')