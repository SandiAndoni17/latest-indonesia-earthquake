import os

import setuptools
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "latest_earthquake_indonesia",
    version = "0.1",
    author = "Sandi Andoni",
    author_email = "sandiandoni17@gmail.com",
    description = ("Athis package will get the latest earthquake from BMKG | Meteorological, Climatological, "
                   "and Geophysical Agency."),

    url = "https://github.com/SandiAndoni17/Early-EarthQuake-Detection",
    #packages=['an_example_pypi_project', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 5- Production/Stable",

    ],
    packages = setuptools.find_packages(),
    python_requires=">=3.12"

)