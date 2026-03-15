# python3
"""
Module Heading XXX
------------------

Some information about this module.

"""

from devtest.qa import bases


class XXXSampleTest(bases.TestCase):
    """
    Purpose
    -------

    The purpose of this test case.

    Pass Criteria
    -------------

    What is the pass criteria?

    Start Condition
    ---------------

    What is the state of the DUT this test needs?

    End Condition
    -------------

    What changes to the condition or state of the DUT are made?

    Reference
    ---------

    Reference to design document or specification clause, or a URI.


    Procedure
    ---------

    #. Step 1 ...
    #. Step 2 ...
    #. Step 3 ...

    """
    # Add the names of other test cases (full path if not in this module), that
    # this case depends on.
    PREREQUISITES: list[str] = []

    # HERE is where your main test logic goes. It may take arguments that are
    # obtained from the suite's add_test() method. You get a global config
    # object in it. Think of that is a bag full of useful stuff. You can use
    # some, none, or all of what is in there. One very useful object is the
    # "environment" attribute that contains the device under test (DUT).
    def procedure(self):
        return self.manual()


class XXXScenario(bases.Scenario):
    """A sample use case that builds a test suite.
    """

    @staticmethod
    def get_suite(config, testbed, ui):
        suite = bases.TestSuite(config, testbed, ui, name="MyNewSuite")
        suite.add_test(XXXSampleTest)
        return suite
