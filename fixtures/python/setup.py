#!/usr/bin/env python
from setuptools import find_packages, setup


setup_args = dict(
    # Description
    name="noos-test",
    version="0.0.1",
    # Package data
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["*tests*"]),
)


if __name__ == "__main__":

    # Make install
    setup(**setup_args)
