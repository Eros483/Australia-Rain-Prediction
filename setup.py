#project management
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements=f.read().splitlines()

setup(
    name="Australia-Weather-Prediction",
    version="0.1",
    author="Arnab",
    packages=find_packages(),
    install_requires=requirements
)