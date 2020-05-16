import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Otter", # Replace with your own username
    version="1.0",
    author="Vitor Hideyoshi",
    author_email="vitor.h.n.batista@gmail.com",
    description="Algebra Functions Python Module for Numeric Calculus",
    long_description=long_description,
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
      ],
)