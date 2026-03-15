"""Example of running remote code.
"""

from devtest.qa import bases


class RemoteCode(bases.TestCase):
    """
    Purpose
    -------

    Demonstrate running remote Python function.

    This one actually runs on the local host.

    Pass Criteria
    -------------

    The function runs and gets the right arguments.

    Start Condition
    ---------------

    Controller is a SelfController.

    End Condition
    -------------

    No change.

    Reference
    ---------

    NA

    Procedure
    ---------

    #. Define a local function in the procedure method.
    #. Invoke the run_python method.
    #. These should be the expected output and no errors.
    """

    def procedure(self):

        def remote_func(arg):
            print("Got arg:", arg)

        def no_args():
            import sys
            print(repr(sys.argv))

        self.info(self.testbed.localhost.device.run_command("hostname -f"))
        resp = self.testbed.localhost.device.run_python(no_args, debug=self.config.flags.debug)
        self.assertEqual(len(eval(resp.strip())), 1)
        resp = self.testbed.localhost.device.run_python(remote_func, 1,
                                                        debug=self.config.flags.debug)
        self.assertEqual(resp, "Got arg: 1\n")
        return self.passed("Ran remote functions as scripts.")
