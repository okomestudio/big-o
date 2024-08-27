"""Plot Big O."""
import math
from collections import namedtuple

import matplotlib.pyplot as plt
import numpy as np
from labellines import labelLine as label_line
from matplotlib import rc, rcParams

rc("text", usetex=True)
rcParams.update({"font.size": 24})

Attr = namedtuple("Attr", ("x", "va"))


def plot_big_o():
    """Plot Big O."""
    xmin, xmax = 0, 32
    plt.figure(figsize=(8.5, 11))

    attrs = []
    xs = np.arange(xmin, xmax, 0.05)

    ys = xs**0.5
    plt.plot(xs, ys, label=r"$\sqrt{n}$")
    attrs.append(Attr(25.0, "bottom"))

    ys = np.log2(xs)
    plt.plot(xs, ys, label=r"$\log{n}$")
    attrs.append(Attr(25.0, "top"))

    ys = xs
    plt.plot(xs, ys, label=r"$n$")
    attrs.append(Attr(22.0, "center"))

    ys = xs * np.log2(xs)
    plt.plot(xs, ys, label=r"$n \log{n}$")
    attrs.append(Attr(12.0, "center"))

    ys = xs**2
    plt.plot(xs, ys, label=r"$n^2$")
    attrs.append(Attr(6.7, "center"))

    ys = 2**xs
    plt.plot(xs, ys, label=r"$2^n$")
    attrs.append(Attr(5.3, "center"))

    xs = np.arange(xmin, xmax, 1, dtype=int)  # arg for factorial must be int
    ys = [math.factorial(x) for x in xs]
    plt.plot(xs, ys, label=r"$n!$")
    attrs.append(Attr(4.22, "center"))

    # Draw
    for line, attr in zip(plt.gca().get_lines(), attrs):
        label_line(line, attr.x, va=attr.va, fontsize=40, align=False)

    axes = plt.gca().axes
    plt.setp(axes.get_xticklabels(), visible=False)
    plt.setp(axes.get_yticklabels(), visible=False)
    axes.tick_params(axis="both", which="both", length=0)

    plt.xlim(1.9, xmax * 0.95)
    plt.ylim(0, 50)

    plt.xlabel(r"$n$")
    plt.title(r"How does $O$ scale as a function of input size?")
    plt.show()
