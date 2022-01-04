import backtrader as bt

class SegmentedCommissionInfo(bt.CommissionInfo):
    """
    This commission is applied if volume is within segment
    """
    params = (
      ('stocklike', True),  # True
      ('commtype', bt.CommInfoBase.COMM_FIXED ),  # % Apply Commission
      # Custom params       
    )    

    segments = []

    def add_segment(self, from_value, to_value, fixed_comm, perc_comm):
      segment = type('segment', (), { 
          "from_value": from_value, 
          "to_value": to_value,
          "fixed_comm": fixed_comm,
          "perc_comm": perc_comm
      })
      self.segments.append(segment)


    def _getcommission(self, size, price, pseudoexec):        
      volume = abs(size) * price
      commvalue = 0.0

      for segment in self.segments:
        if ( 
            ( ( segment.from_value is None ) or (segment.from_value <= volume ) ) 
            and
            ( ( segment.to_value is None) or (volume <= segment.to_value) )
          ):
          fixed = segment.fixed_comm
          variable = segment.perc_comm * volume
          commvalue = fixed + variable           

      if not pseudoexec:
          # keep track of actual real executed operation
          pass    
      
      return round(commvalue, 6)

PB = 1.0/10000.0