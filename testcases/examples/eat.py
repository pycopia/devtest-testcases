"""
Eat
---

Example test case. Manual test to instruct runner to eat something.
"""

from typing import ClassVar
from devtest.qa import bases


class EatTheApple(bases.TestCase):
    """
    Purpose
    -------

    Demonstrate eating an apple. This is an interactive, manual test.

    Pass Criteria
    -------------

    The apple is eaten.

    Start Condition
    ---------------

    empty stomach.

    End Condition
    -------------

    Stomach full of apple.

    Reference
    ---------

    Gray's Anatomy.

    Procedure
    ---------

    1. Open mouth
    2. Place apple to mouth
    3. Bite with teeth
    4. Chew
    5. swallow
    6. repeat steps 1 through 5 until apple is gone.
    """

    INTERACTIVE: ClassVar[bool] = True

    def procedure(self):
        return self.manual()


class EatingScenario(bases.Scenario):
    """Eating the apple use case.

    A use case typically constructs a TestSuite containing a set of tests for
    this particular use case. The ``get_suite`` method takes a config and
    environment that it can use to adjust the set of test.
    """

    @staticmethod
    def get_suite(config, environment, ui):
        suite = bases.TestSuite(config, environment, ui, name="EatingSuite")
        suite.add_test(EatTheApple)
        return suite
