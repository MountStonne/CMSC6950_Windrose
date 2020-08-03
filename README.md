# CMSC6950_Windrose
CMSC6950 Course Project by Shuo Wang

## Introduction
A wind rose is a graphic tool to describe the wind speed and direction distribution at a particular location.

Windrose, a Python library to implement wind analysis, will be used to plot windroses and fit Weibull probability density functions.

Windrose package link: https://github.com/python-windrose/windrose

A python package named

## Install

### Requirements

- matplotlib http://matplotlib.org/
- numpy http://www.numpy.org/
- and naturally python https://www.python.org/
- Pandas http://pandas.pydata.org/ (to feed plot functions easily)

### Install latest release version via pip

A package is available and can be downloaded from PyPi and installed using:

```bash
$ pip install windrose
```

### Install latest development version

```bash
$ pip install git+https://github.com/python-windrose/windrose
```

or

```bash
$ git clone https://github.com/python-windrose/windrose
$ python setup.py install
```

## Reproducibility
To regenerate this report, clone this repo:
```bash
$ git clone https://github.com/MountStonne/CMSC6950_Windrose
```
Then regenerate using:
```bash
$ make
```