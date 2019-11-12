# -*- coding: utf-8 -*-

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ElegooMarsUtility",
    version="0.2",
    author="Jan Mrázek",
    author_email="email@honzamrazek.cz",
    description="Utility to post process sliced models for Elegoo Mars",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yaqwsx/ElegooMarsUtility",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "click",
        "numpy",
        "pyphotonfile>=0.2",
        "scikit-image",
        "Pillow==6.2.0"
    ],
    zip_safe=False,
    include_package_data=True,
    entry_points = {
        "console_scripts": [
            "elegooMarsUtility=elegooMarsUtility.main:cli"
        ],
    }
)