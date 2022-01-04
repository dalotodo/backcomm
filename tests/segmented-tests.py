import unittest

import backcomm

class TestSegmentedCommissionInfo(unittest.TestCase):

    def setUp(self):
        comm = backcomm.SegmentedCommissionInfo()
        # Hasta 300 €	1,10 €
        comm.add_segment(None, 300.0, 1.45, 0.0)
        # De 300 a 3.000 €	2,45 € + 2,4PB
        comm.add_segment(300.0, 3000.0, 2.45, 2.4 * backcomm.PB)
        # De 3.000 a 35.000 €	4,65 € + 1,2PB
        comm.add_segment(3000.0, 35000.0, 4.65, 1.2 * backcomm.PB)
        # De 35.000 a 70.000 €	6,40 € + 0,7PB
        comm.add_segment(35000.0, 70000.0, 6.40, 0.7 * backcomm.PB)
        # De 70.000 a 140.000 €	9,20 € + 0,3PB
        comm.add_segment(70000.0, 140000.0, 9.20, 0.3 * backcomm.PB)
        # Más de 140.000,01 €	13,40 €
        comm.add_segment(140000.0, None, 13.40, 0.0)

        self.comm = comm

    def test_segments(self):        
        testcases = [
          { 'qty': 299, 'price': 1, 'expected': 1.4500 },
          { 'qty': 300, 'price': 1, 'expected': 2.5220 },
          { 'qty': 3000, 'price': 1, 'expected': 5.01 },
          { 'qty': 150000, 'price': 1, 'expected': 13.40 },
        ]

        for testcase in testcases:
          result = self.comm._getcommission( testcase['qty'], testcase['price'], True)
          self.assertEqual(result, testcase['expected'])

    def test_negatives(self):
        testcases = [
          { 'qty': -299, 'price': 1, 'expected': 1.4500 },
          { 'qty': -300, 'price': 1, 'expected': 2.5220 },
          { 'qty': -3000, 'price': 1, 'expected': 5.01 },
          { 'qty': -150000, 'price': 1, 'expected': 13.40 },
        ]

        for testcase in testcases:
          result = self.comm._getcommission( testcase['qty'], testcase['price'], True)
          self.assertEqual(result, testcase['expected'])