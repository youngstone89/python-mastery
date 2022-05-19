import mastery
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



setup(
    name="python-mastery",
    version=mastery.__version__,
    description='Python Mastery Project',  # Optional
    author='youngstone89',  # Optional
    author_email='youngstone89@icloud.com',  # Optional

    packages=find_packages( # Required
        where='.',
        include=["*"],
        exclude=[]
    ),
    python_requires='>=3.8, <4',
    install_requires=requirements,
    project_urls={  # Optional
        'Source': 'https://github.com/youngstone89/python-mastery',
    },
)