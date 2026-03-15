"""Demo module for showing some framework features.

Provides a special test case that enters an interactive prompt within the test
procedure. The user can then invoke any method and inspect to config and
testbed interactively. Useful for demos and learning the API.
"""

from devtest.qa import bases
from devtest.qa import repl


class InteractiveTest(bases.TestCase):
    """
    Purpose
    -------

    Enable direct interaction of the framework API.

    Pass Criteria
    -------------

    None

    Start Condition
    ---------------

    NA

    End Condition
    -------------

    No change.

    Reference
    ---------

    None

    Procedure
    ---------

    #. Start an interactive interpreter in the context of the execute method.
    """

    def procedure(self, argument=None):
        cons = repl.InteractiveConsole(namespace=locals(), ps1="TestCase> ",
                                       history="~/.hist_testcase")
        cons.interact(banner="Now try out the methods and other functions.")
