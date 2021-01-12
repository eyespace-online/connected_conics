# Connected Conics

A library for geometric analysis of connected conic sections.

## Usage

Install from PyPI
Also install matplotlib (optional) to generate a plot for this example.

```bash
pipenv install connected_conics
pipenv install matplotlib
```

```python
import yaml
import numpy
import matplotlib.pyplot as plt
from connected_conics import conic, helpers

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
X = numpy.linspace(0, 6, 1000)
Y = conic.find_val_vectorized(c["rs"], c["es"], c["hds"], c["offsets"], X)
plt.figure()
plt.plot(X, Y)
plt.show()
```

## Local development

```bash
git checkout ...
pipenv install --dev
pipenv install -e .
pipenv shell
py.test
```

## Deployment

```bash
python setup.py sdist bdist_wheel
twine upload dist/*
```

Copyright 2020 Innovatus Technology Pty Ltd
