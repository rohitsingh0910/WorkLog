# setup.py
from setuptools import setup
from Cython.Build import cythonize

setup(
    name="py2c",
    ext_modules=cythonize("converter.pyx", compiler_directives={"language_level": "3"}),
)
