import os
import sys
from setuptools import setup, find_packages

# Ensure the root directory is in the import path
sys.path.insert(0, os.path.abspath("."))

# Read dependencies
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='oopoa',
    version='0.1.0',
    description='OOPOA CLI Tool (Object-Oriented Programming Optimization Algorithm)',
    author='LA-10',
    py_modules=["main"],                      # Register main.py at root
    packages=find_packages(),  # Detect 'commands/' as a package
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'oopoa = main:cli'                # maps 'oopoa' to cli() in main.py
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
