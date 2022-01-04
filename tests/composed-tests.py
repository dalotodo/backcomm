import unittest

import backtrader as bt
import backcomm as bc

class TestComposedCommissionInfo(unittest.TestCase):
    

    def test_fixed(self):        
        comm = bc.ComposedCommissionInfo()
        comm.add_commission( bt.CommissionInfo(commission=0.5) )

        testcases = [          
          { 'qty': 100, 'price': 1, 'expected': 50 },          
        ]

        for testcase in testcases:
          result = self.comm._getcommission( testcase['qty'], testcase['price'], True)
          self.assertEqual(result, testcase['expected'])
    