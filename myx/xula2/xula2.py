
import myhdl
from myhdl import Signal, intbv
from rhea.build.boards.xilinx import Xula2

class StickIt(Xula2):
    def __init__(self, led_pmod=2, sseg_pmod=4):
        # update the port definitions with the PMOD 
        # specific information
        assert led_pmod in (2, 4, 6)
        
        super(StickIt, self).__init__()

        if led_pmod == 2:
            ledpmod = {"led": dict(pins=('R7',)),
                       "button": dict(pins=('M16',)),
                   }
        elif led_pmod == 4:
            pass

        self.default_ports.update(ledpmod)
        
    def build(self, top):
        brd = self
        flow = get_flow(top)
        flow.run()
        
        