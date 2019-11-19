# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:21:29 2019

@authors: Alexis Ayme, Quentin Mascart, Sofiane Ettayeb, Romain Ilbert, Tristan Capillon 
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "projet_visu",
    version = "1.0",
    author = "Alexis Ayme",
    author_email="alexis.ayme@ensae.fr", "tristan.capillon@ensae.fr", "quentin.mascart@ensae.fr", "romain.ilbert@ensae.fr", "sofiane.ettayeb@ensae.fr"
    description = "A small example package",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
