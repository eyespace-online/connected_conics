import os
import tempfile
import logging
import numpy
import pytest
import json
import yaml
from time import perf_counter
from connected_conics import conic, helpers


def test_predefined_conic():
    with open("tests/sample_conic.json") as f:
        data = json.load(f)
    fullspec_dict = data["fullspec"]
    c = helpers.get_conic_from_fullspec(fullspec_dict, 0)
    X = numpy.linspace(0, 6, 1000)
    Y = conic.find_val_vectorized(c["rs"], c["es"], c["hds"], c["offsets"], X)
    assert numpy.amax(abs(data["X"] - X)) == 0
    assert numpy.amax(abs(data["Y"] - Y)) == 0


def test_time():
    fullspec = """
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
    fullspec_dict = yaml.safe_load(fullspec)
    c = helpers.get_conic_from_fullspec(fullspec_dict, 0)
    t1 = perf_counter()
    X = numpy.linspace(0, 6, 1000)
    Y = conic.find_val_vectorized(c["rs"], c["es"], c["hds"], c["offsets"], X)
    t2 = perf_counter()
    print("Elapsed: {}".format(t2 - t1))
