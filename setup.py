#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import os
from setuptools import setup, find_packages


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setup(
    name="humble_downloader",  # your package name (i.e. for import)
    version="0.5.0",
    maintainer="Mayeul Cantan",
    maintainer_email="mayeul.cantan@live.fr",
    author="Brian Schkerke, Mayeul Cantan",
    author_email="N/A, mayeul.cantan@live.fr",
    description="An automated utility to download your Humble Bundle purchases.",
    license="MIT",
    keywords="humble bundle download games",
    url="https://github.com/MayeulC/hb-downloader",
    packages=find_packages(exclude=["*test*", "*TEST*"]),
    install_requires=[
        'requests',
        'pyyaml',
    ],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT",
        "Natural Language :: English"
    ],
    zip_safe=True,
)
