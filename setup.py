import setuptools
import os

__name = "yoshi-otter"

__version_sufix = os.environ.get('VERSION_SUFIX')
if not __version_sufix:
    __version_sufix = "dev"

__version = f"2.0.{__version_sufix}"

with open("README.md", "r") as fh:
    __long_description = fh.read()

setuptools.setup(
    name=__name,
    version=__version,
    author="Vitor Hideyoshi",
    author_email="vitor.h.n.batista@gmail.com",
    description="Numeric Calculus python module in the topic of Algebra Functions",
    long_description=__long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HideyoshiNakazone/Otter-NumericCalculus.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pandas',
        'yoshi-seals'
    ],
)
