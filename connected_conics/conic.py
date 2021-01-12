"""
This contains all the code required to plot conic sections and join conics together.
We use the convention: e for single value, es for vector value.

e: eccentricity
r: radius of curvature
hds: Stands for "half diameter". Contact lenses specifications are usually in terms of diameter (i.e. chord width), but that's not much use here. We use half-diameter (i.e. the x value).
"""

import numpy
import math


def sag(roc, e, x):
    if e == 1:
        return (x * x) / (2 * roc)
    num = roc - numpy.sqrt(roc * roc - (1.0 - e * e) * numpy.multiply(x, x))
    den = 1.0 - e * e
    res = num / den
    return res


def calc_offsets(rs, es, hds):
    offsets = [0] * len(rs)
    if len(rs) > 1:
        for idx in range(1, len(rs)):
            s1 = sag(roc=rs[idx - 1], e=es[idx - 1], x=hds[idx - 1])
            s2 = sag(roc=rs[idx], e=es[idx], x=hds[idx - 1])
            offsets[idx] = offsets[idx - 1] + s1 - s2
    return offsets


def find_zone(hds, x):
    for idx in range(len(hds) - 1, -1, -1):
        if x > hds[idx]:
            return idx + 1
    return 0


def find_val(rs, es, hds, offsets, x):
    zone = int(find_zone(hds, x))
    return sag(roc=rs[zone], e=es[zone], x=x) + offsets[zone]


def find_val_vectorized(rs, es, hds, offsets, X):
    v = numpy.vectorize(find_val, excluded=["rs", "es", "hds", "offsets"])
    return v(rs=rs, es=es, hds=hds, offsets=offsets, x=X)
