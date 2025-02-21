from setuptools import setup, find_packages

setup(
    name="quickbio",
    version="0.1.0",
    packages=find_packages(),
    description="A lightweight bioinformatics toolkit",
    author="Sriram Hathwar",
    author_email="hathwar.sj@gmail.com",
    url="https://github.com/hathwars/quickbio",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    python_requires=">=3.6",
)