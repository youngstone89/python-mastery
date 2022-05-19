import package2
from setuptools import setup, find_packages
import os

packages = find_packages()
print(packages)


PKG='src'
filepath = os.path.abspath(__file__)
dirname = os.path.dirname(filepath)
pkgpath = os.path.join(dirname,PKG)
print(filepath)
print(dirname)
print(pkgpath)


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


here = os.path.abspath(os.path.dirname(__file__))


setup(
    name="python-mastery",
    version=package2.__version__,
    description='Python Mastery Project',  # Optional
    packages=find_packages(
        where='.',
        include=["*"],
        exclude=[]
    ),
)