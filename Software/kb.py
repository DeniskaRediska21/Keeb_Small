import board
import digitalio

from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner

# VBus pin config
VBUS_PIN = board.VBUS_SENSE  # RPi Pico
# VBUS_PIN = board.GP29      # WeAct RP2040 + resistors on Piantor PCB

# split side detection using vbus sense
# vbus = digitalio.DigitalInOut(VBUS_PIN)
# vbus.direction = digitalio.Direction.INPUT
# isRight = False if vbus.value == True else False
# isRight = False


# alternate option: set side based on drive names
name = str(getmount('/').label)
isRight = True if name.endswith('R') else False

# GPIO to key mapping, Left
_KEY_CFG_LEFT = [
board.GP21,board.GP18,board.GP17,board.GP9,board.GP6,
board.GP22,board.GP19,board.GP16,board.GP10,board.GP7,
board.GP26,board.GP20,board.GP13,board.GP11,board.GP8,
board.GP4,board.GP5
]

# GPIO to key mapping, Left
_KEY_CFG_RIGHT = [
board.GP6,board.GP9,board.GP17,board.GP18,board.GP21,
board.GP7,board.GP10,board.GP16,board.GP19,board.GP22,
board.GP8,board.GP11,board.GP13,board.GP20,board.GP26,
board.GP5,board.GP4
]

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
            pins = _KEY_CFG_RIGHT if isRight == True else _KEY_CFG_LEFT
        )

    # flake8: noqa
    # fmt: off
    coord_mapping = [
0,1,2,3,4,17,18,19,20,21,5,6,7,8,9,22,23,24,25,26,10,11,12,13,
14,27,28,29,30,31,15,16,32,33]
