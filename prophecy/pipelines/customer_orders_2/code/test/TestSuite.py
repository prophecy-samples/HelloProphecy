import unittest

from test.customer_orders_2.graph.test_By_CustomerId import *
from test.customer_orders_2.graph.test_Cleanup import *

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite())
