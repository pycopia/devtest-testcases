from setuptools import setup

NAME = "devtest-testcases"
VERSION = "1.0"

setup(
    name=NAME,
    version=VERSION,  # not used when setuptools_scm is used, but seems to be required.
    namespace_packages=["testcases"],
    packages=["testcases.examples"],
)
