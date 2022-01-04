import unittest

import backtrader as bt
import backcomm as bc

class TestComposedCommissionInfo(unittest.TestCase):
    

    def test_composition(self):        
        comm = bc.ComposedCommissionInfo()
        # 5% Commission
        comm.add_commission( bt.CommissionInfo(stocklike=True, commission=0.05) )
        # 10 monetary units Fixed fee Commission
        comm.add_commission( bc.FixedCommissionInfo(commission=10.0) )

        testcases = [          
          { 'qty': 100, 'price': 1, 'expected': 15 },
        ]

        for testcase in testcases:
          result = comm._getcommission( testcase['qty'], testcase['price'], True)
          self.assertEqual(result, testcase['expected'])
    