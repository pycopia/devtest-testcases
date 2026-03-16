from setuptools import setup

NAME = "devtest-testcases"

REQUIREMENTS = [s.strip() for s in open("requirements.txt").readlines()]

setup(
    name=NAME,
    # version=VERSION,  # not used when setuptools_scm is used.
    namespace_packages=["testcases"],
    packages=["testcases.examples"],
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    install_requires=REQUIREMENTS,
)
