

import myhdl
from myhdl import Signal, intbv


def blinky(clock, led, button):
    """A simple LED blink example.
    This is intended to be used with the Xula2+StickIt motherboard
    and an LED+button PMOD board.

    Arguments (ports):
        clock: 12MHz external clock
        led: the LED port/pin
        button: the button port/pin

    Parameters:
        pmod: select which PMOD connector the PMOD is connected
    """
    
    maxcnt = int(clock.frequency) // 4
    cnt = Signal(intbv(0, min=0, max=maxcnt))
    toggle = Signal(bool(0))

    @always(clock.posedge)
    def beh_toggle():
        if cnt >= maxcnt-1:
            toggle.next = not toggle
            cnt.next = 0
        else:
            cnt.next = cnt + 1

    @always_comb
    def beh_assign():
        if not button:
            led.next = True
        else:
            led.next = toggle

    return beh_toggle, beh_assign