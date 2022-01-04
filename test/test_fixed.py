import unittest

import backtrader as bt
import backcomm as bc

class TestFixedCommissionInfo(unittest.TestCase):
    

    def test_composition(self):        
        COMM = 10.0
        comm = bc.FixedCommissionInfo(commission=COMM)

        testcases = [          
          { 'qty': 100, 'price': 1, 'expected': COMM },          
          { 'qty': 100, 'price': 100, 'expected': COMM },          
          { 'qty': -100, 'price': 10, 'expected': COMM },          
          
        ]

        for testcase in testcases:
          result = comm._getcommission( testcase['qty'], testcase['price'], True)
          self.assertEqual(result, testcase['expected'])
    