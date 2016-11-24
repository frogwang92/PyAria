import unittest
import broker.backtestbroker as broker


class BrokerTest(unittest.TestCase):
    initmoney = 10000.0

    def setUp(self):
        self.broker = broker.BackTestBroker()
        self.portfolio = broker.Portfolio(money=BrokerTest.initmoney)
        self.portfolio.subscribe_to_broker(self.broker)

    def tearDown(self):
        pass

    def testbuy(self):
        """test case of buy"""
        self.broker.buy(2.0, 1000.0)
        self.assertEqual(self.portfolio.money, BrokerTest.initmoney - 1000.0)
        self.assertEqual(self.portfolio.holds, 1000/2.0)

    def test2times(self):
        self.broker.buy(2.0, 1000.0)
        self.broker.buy(price=3.0, money=2000.0)
        self.assertEqual(self.portfolio.money, BrokerTest.initmoney - 1000.0 - 2000.0)
        self.assertEqual(self.portfolio.holds, 1000 / 2.0 + 2000.0 / 3.0)

    def testsell(self):
        self.broker.sell(5.0, 100.0)
        self.assertEqual(self.portfolio.money, 5.0 * 100.0 + 10000.0)
        self.assertEqual(self.portfolio.holds, -100.0)

    def testbuyandsell(self):
        self.broker.buy(3.0, 1000.0)
        self.broker.sell(5.0, 100.0)
        self.assertEqual(self.portfolio.money, BrokerTest.initmoney - 1000.0 + 5.0 * 100.0)
        self.assertEqual(self.portfolio.holds, 1000.0 / 3.0 - 100.0)

if __name__ == '__main__':
    unittest
