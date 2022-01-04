import backtrader as bt

class ComposedCommissionInfo(bt.CommissionInfo):
    """
    Applies the sum of all commissions it contains
    """
    params = (
      ('stocklike', True),  # True
      ('commtype', bt.CommInfoBase.COMM_FIXED ),  # % Apply Commission
      # Custom params       
    )    

    commissions = []

    def add_commission(self, comm):
      if isinstance(comm,bt.CommissionInfo):
        self.commissions.append(comm)
      else:
        raise TypeError("Invalid commission type")


    def _getcommission(self, size, price, pseudoexec):              
      totalvalue = 0.0

      for commission in self.commissions:
        commvalue = commission._getcommission(size,price,pseudoexec)
        totalvalue += commvalue

      if not pseudoexec:
          # keep track of actual real executed operation
          pass    
      
      return round(totalvalue, 6)
