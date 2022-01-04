import backtrader as bt

class FixedCommissionInfo(bt.CommissionInfo):
    '''
    Fixed commission
    '''
    params = (
        ('commission', 0.0),
        ('stocklike', True),
        ('commtype', bt.CommInfoBase.COMM_FIXED),
        )

    def _getcommission(self, size, price, pseudoexec):
        return self.p.commission