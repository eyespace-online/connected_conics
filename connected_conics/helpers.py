from . import conic, helpers, surf
import math
import json
import numpy as np


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


def get_sagf_from_fullspec(fullspec):
    lens = []
    for idx, val in enumerate(fullspec[0]["r"]):
        c = get_conic_from_fullspec(fullspec, idx)
        lens.append(c)
    sag_vector = np.vectorize(lens_sag, excluded=["lens"])
    return lambda RHO, PHI: sag_vector(lens=lens, r=RHO, theta=PHI)


def get_conic_from_fullspec(rows, m):
    """
    Extracts a dict describing the conic section of meridian n from our fullspec definition.

    Where rows is a dict representing:

    - r: [8]
      e: [0.0]
      d: 6.0
    - r: [9]
      e: [0.5]
      d: 10.0
    - r: [11]
      e: [1.1]
      d: 12.0
    """
    rs = [0] * len(rows)
    es = [0] * len(rows)
    hds = [0] * len(rows)
    for idx, row in enumerate(rows):
        hds[idx] = row["d"] / 2.0
        rs[idx] = row["r"][m]
        es[idx] = row["e"][m]
    offsets = conic.calc_offsets(rs, es, hds)
    output = {}
    output["hds"] = hds
    output["es"] = es
    output["rs"] = rs
    output["offsets"] = offsets
    return output


def lens_sag(lens, r, theta):
    """
    Returns the sag of the lens at a given point.

    Args:
        lens: The first parameter.
        param2: The second parameter.

    Returns:
        Sag of the lens, or nan if point is outside lens.

    """
    if r < 0:
        r = abs(r)
        theta = theta + math.pi
    if r > lens[0]["hds"][-1]:
        return np.nan
    if len(lens) == 1:
        lens_val = conic.find_val(
            lens[0]["rs"], lens[0]["es"], lens[0]["hds"], lens[0]["offsets"], r
        )
    elif len(lens) == 2:
        l1 = conic.find_val(
            lens[0]["rs"], lens[0]["es"], lens[0]["hds"], lens[0]["offsets"], r
        )
        l2 = conic.find_val(
            lens[1]["rs"], lens[1]["es"], lens[1]["hds"], lens[1]["offsets"], r
        )
        lens_val = surf.interp_sag(l1, l2, (theta))
    return lens_val


def to_fullspec(rs, es, hds):
    """
    Rotationally symmetric dump of a list of each to fullspec
    """
    output = []
    for idx in range(0, len(rs)):
        row = {"r": [rs[idx]], "e": [es[idx]], "d": hds[idx] * 2}
        output.append(row)
    return output


def get_lens_from_fullspec(rows):
    """
    Same as get_conic_from_fullspec, but gets a list
    """
    rs = [0] * len(rows)
    es = [0] * len(rows)
    hds = [0] * len(rows)

    outputs = []
    for m in range(0, len(rows[0]["r"])):
        output = {}
        for idx, row in enumerate(rows):
            hds[idx] = row["d"] / 2.0
            rs[idx] = row["r"][m]
            es[idx] = row["e"][m]
        offsets = conic.calc_offsets(rs, es, hds)
        output["hds"] = hds
        output["es"] = es
        output["rs"] = rs
        output["offsets"] = offsets
        outputs.append(output)
    return outputs
