# Package Distribution Introduction
Package used as an exemple for my presentation at ProgFest 2022 Ulaval.

## Useful commands to publish a package on PyPI or TestPyPI

### Create source distribution

```
pip install twine wheel build
```

```
python -m build
```

#### Upload to PyPI

Make sure to register to [PyPI](https://pypi.org/account/register/) first.

```
python -m twine check dist/*
```

```
python -m twine upload dist/*
```

### Upload to TestPyPI

Make sure to register to [TestPyPI](https://test.pypi.org/account/register/) first.

```
python -m twine upload --repository testpypi dist/*
```
