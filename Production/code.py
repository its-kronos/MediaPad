import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners.keyboard import KeysScanner
from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap
from kmk.extensions.media_keys import MediaKeys

'''boardLockPin = 4

backTrackPin=27
rewindPin=28
pausePin=29
fastForwardPin=6
forwardTrackPin=7

soundControlPin = 0

rotaryA=2
RotaryB=1'''

board_lock = False
volume_lock = False

keyboard = KMKKeyboard()
encoder = EncoderHandler()
macro = Macros()
keyboard.modules = [encoder,macro,MediaKeys()]

switchPins = [
    board.GP4, #boardLock
    board.GP27, #backtrack
    board.GP28, #rewind
    board.GP29,# pause
    board.GP6,#fast forward
    board.GP7,#skip track
    board.GP0#sound control
]

keyboard.matrix = KeysScanner(
    pins=switchPins,
    value_when_pressed =False
)


def backTrackFunction():
    if not board_lock:
        Press(KC.LSHIFT)
        Tap(KC.P)
        Release(KC.LSHIFT)

backTrackMacro = KC.MACRO(
    on_press = backTrackFunction
)


def skipTrackFunction():
    if not board_lock:
        Press(KC.LSHIFT)
        Tap(KC.N)
        Release(KC.LSHIFT)

skipTrackMacro = KC.MACRO(
    on_press = skipTrackFunction
)


def boardLockFunction():
    global board_lock
    board_lock = not board_lock

boardLockMacro = KC.MACRO(
    on_press = boardLockFunction
)

keyboard.keymap = [
    [boardLockMacro,backTrackMacro,KC.LEFT,KC.SPACE,KC.RIGHT,skipTrackMacro,None]
]



encoder.pins = (
    (board.GP2,board.GP1,board.GP0)
)

def volumeLockFunction():
    global volume_lock
    volume_lock = not volume_lock

volumeLockMacro = KC.MACRO(
    on_press = volumeLockFunction
)


def volumeDownFunction():
    if not volume_lock:
        Tap(KC.VOLD)

volumeDownMacro = KC.MACRO(
    on_press = volumeDownFunction
)


def volumeUpFunction():
    if not volume_lock:
        Tap(KC.VOLU)

volumeUpMacro = KC.MACRO(
    on_press=volumeUpFunction
)

encoder.map = [(
    (volumeDownMacro,volumeUpMacro,volumeLockMacro)
)]


if __name__ == "__main__":
    keyboard.go()



