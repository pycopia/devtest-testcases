"""
Framework readiness and demo tests.
--------

Test cases here that show and verify that the framework is working and reports
are being output.

Can be used to demo output styles.

Test case plans are in the form of docstrings here. They are parsed as
reStructuredText by other tools.
"""

from devtest.qa import bases


class BasicReadinessCheck(bases.TestCase):
    """
    Purpose
    -------

    Verify that any test case can be run by the framework.

    Pass Criteria
    -------------

    You can read this text.

    Start Condition
    ---------------

    None

    End Condition
    -------------

    No change.

    Reference
    ---------

    None


    Procedure
    ---------

    #. Read this text.
    #. Answer yes to the following questions.
    """

    def procedure(self):
        return self.manual()


class PassCheck(bases.TestCase):
    """
    Purpose
    -------

    Verify proper pass reporting.

    Pass Criteria
    -------------

    This test passes.

    Start Condition
    ---------------

    None

    End Condition
    -------------

    No change.

    Reference
    ---------

    None


    Procedure
    ---------

    #. Return a passed indication.
    """

    def procedure(self):
        return self.passed("Always passes")


class FailCheck(bases.TestCase):
    """
    Purpose
    -------

    Verify proper fail reporting.

    Pass Criteria
    -------------

    This test fails, and a non-zero is passed back to shell running the
    test runner (devtester).

    Start Condition
    ---------------

    None

    End Condition
    -------------

    No change.

    Reference
    ---------

    None


    Procedure
    ---------

    #. Return a failure indication.
    """

    def procedure(self):
        return self.failed("Always fails")


class ErrorCheck(bases.TestCase):
    """
    Purpose
    -------

    Verify proper error reporting and debugging.

    Pass Criteria
    -------------

    This test throws an error.

    Start Condition
    ---------------

    None

    End Condition
    -------------

    No change.

    Reference
    ---------

    None


    Procedure
    ---------

    #. Raise an arbitrary ValueError exception.
    #. Observe how it is reported as *incomplete*.
    #. Verify that a debugger is started when using the *-d* flag.
    """

    def procedure(self):
        self.info("Raising an exception.")
        _raise_error()
        return self.passed("Always passes, but this is not reached.")


def _raise_error():
    raise ValueError("Some bogus value.")


class WithData(bases.TestCase):
    """
    Purpose
    -------

    Verify proper recording of data.

    Pass Criteria
    -------------

    The data is recorded without error.

    Procedure
    ---------

    #. Add some data with the record_data method.
    """

    def procedure(self):
        self.info("Adding some data.")
        self.record_data({"data": "dict"})
        self.info("Adding some more data.")
        self.record_data({"more": "data"})
        return self.passed(
            "Added data. There should be a list of two dicts in data output.")


class DemoScenario(bases.Scenario):
    """A scenario that can be used to demonstrate framework features.
    """

    @staticmethod
    def get_suite(config, environment, ui):
        suite = bases.TestSuite(config, environment, ui, name="DemoSuite")
        suite.add_tests([
            BasicReadinessCheck,
            PassCheck,
        ])
        if config.get("dofailure", False):
            suite.add_test(FailCheck)
        return suite


class PassFailErrorScenario(bases.Scenario):
    """A scenario that can be used to demonstrate framework features.
    """

    @staticmethod
    def get_suite(config, environment, ui):
        suite = bases.TestSuite(config, environment, ui, name="DemoSuite")
        suite.add_test(PassCheck)
        suite.add_test(FailCheck)
        suite.add_test(ErrorCheck)
        return suite
