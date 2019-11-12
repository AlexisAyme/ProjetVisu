# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:21:29 2019

@author: aymea
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="projet_visu",
    version="1.0",
    author="Alexis Ayme",
    author_email="alexis.ayme@ensae.fr",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
