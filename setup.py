#!/usr/bin/env python3
# License: MIT License
# Copyright (C) 2020 Jochen Steimel
import os
from setuptools import setup

AUTHOR_NAME = "Jochen Steimel"
AUTHOR_EMAIL = "jochen.steimel@googlemail.com"


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return "File '%s' not found.\n" % fname


setup(
    name="pyflowsheet",
    version="0.2.0",
    description="A Python library for creating process flow diagrams (PFD) for process engineering using SVG drawings.",
    author=AUTHOR_NAME,
    email=AUTHOR_EMAIL,
    url="https://github.com/nukleon84/pyflowsheet",
    python_requires=">=3.7",
    packages=["pyflowsheet"],
    provides=["pyflowsheet"],
    long_description=read("readme.md") + read("changelog.md"),
    long_description_content_type="text/markdown",
    platforms="OS Independent",
    license="MIT License",
    install_requires=["svgwrite", "pathfinding"],
    extras_require={"plots": ["matplotlib"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
    project_urls={
        "Bug Reports": "http://github.com/nukleon84/pyflowsheet/issues",
        "Source": "http://github.com/nukleon84/pyflowsheet/",
    },
)