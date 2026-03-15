# Base Test Cases for Devtest

This package is intended to work with the [devtest](https://github.com/pycopia/devtest) system test
framework. The devtest framework uses this as the base package name to find test cases to run.

This package is a _setuptools_-style namespace package that establishes the *testcases* namespace.

Other package distributions may use the *testcases* base package namespace to install additional
test cases for any project.  All such packages then share a common base package name that the
*devtest* framework can find.

This project may also be used as a template for other testcases packages. Since it uses the
*setuptools*' namespace feature, all such packages will have the root package name of "testcases".
The *devtest* framework, by default, searches for test case implementations in this namespace.

This package also provides some example test cases for trying out the test runner.

There is also the `_template.py` file here that you may use as a test case template for writing new
test case modules.
