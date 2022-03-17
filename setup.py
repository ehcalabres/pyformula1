# Copyright 2022, ehcalabres @ Github
# See LICENSE for details

from setuptools import setup, find_packages


def read_file(filename):
    with open(filename, "r+") as f:
        return f.read()


def get_requirements(filename):
    requirements = list()
    with open(filename, "r+") as f:
        for line in f.readlines():
            requirements.append(line.strip())
    return requirements


setup(
    name="pyformula1",
    version="0.0.1",
    description="Retrieval F1 historical data tool from https://ergast.com/mrd/ for Python",
    long_description=read_file(filename="README.md"),
    long_description_content_type="text/markdown",
    author="Enrique Hernández Calabrés",
    author_email="ehcalabres@gmail.com",
    license="MIT License",
    install_requires=get_requirements(filename="requirements/requirements.txt"),
    include_package_data=True,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries"
    ],
    keywords="F1 formula1 formula-1 sports historical-data racing cars motorsport",
    project_urls={
        "Bug Reports": "https://github.com/ehcalabres/pyformula1/issues",
        "Source": "https://github.com/ehcalabres/pyformula1"
    }
)
