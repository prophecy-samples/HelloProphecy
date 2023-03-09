import unittest

from test.job.graph.test_By_CustomerId import *
from test.job.graph.CleanupSubgraph.test_Cleanup import *

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite())
