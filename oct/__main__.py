import os
import sys
import argparse

from pyats import easypy
from pyats.easypy.main import EasypyRuntime

from oct.tests import mandatory_test_arguments
from settings import email, customer_password


TSTDIR = os.path.join(os.path.dirname(__file__), "tests")
DTFDIR = os.path.join(TSTDIR, "datafile")

test_script = {
    "script": os.path.join(TSTDIR, "test_script.py"),
    "datafile": os.path.join(DTFDIR, "common_data.yaml")
}


def main(runtime: EasypyRuntime):

    testbed = runtime.testbed
    easypy.run(
        testscript=test_script["script"],
        datafile=test_script["datafile"],
        email=email,
        password=customer_password,
        **mandatory_test_arguments(testbed)
    )


if __name__ == "__main__":
    # This configuration allow to replace `easypy` with a Python runner.
    #
    # It means that
    #    easypy oct/__main__.py <...>
    # you can replace with
    #    python -m oct <...>
    # where <...> are easypy's arguments.
    #
    # We add a name of this module as first parameter to the `sys.argv`
    # as `easypy` expect it as positional parameter.
    sys.argv = [sys.argv[0]] + sys.argv
    easypy.main()
