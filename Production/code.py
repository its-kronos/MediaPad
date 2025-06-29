import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners.keypad import KeysScanner
from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import Key

'''
soundControlPin = 0 (TO CHANGE)

rotaryA=2 (TO CHANGE)
RotaryB=1 (TO CHANGE)'''

board_lock = False
volume_lock = False

keyboard = KMKKeyboard()
encoder = EncoderHandler()
macro = Macros()
keyboard.modules = [encoder,macro,MediaKeys()]

switchPins = [
    board.D9, #boardLock
    board.D1, #backtrack
    board.D2, #rewind
    board.D3,# pause
    board.D4,#fast forward
    board.D5,#skip track
    board.D6#sound control
]

keyboard.matrix = KeysScanner(
    pins=switchPins,
    value_when_pressed =False
)



class TrackClass(Key):
    def __init__(self,key):
        self.key = key
    def on_press(self,keyboard,key):
        if not board_lock:
            keyboard.tap_key(KC.LSHIFT(self.key))
    def on_release(self, keyboard, key):
        pass
        
backTrack = TrackClass(KC.P)
skipTrack = TrackClass(KC.N)


class boardLockClass(Key):
    def on_press(self,keyboard,key):
        global board_lock
        board_lock = not board_lock
        print(board_lock)
    def on_release(self, keyboard, key):
        pass

boardLock = boardLockClass()

keyboard.keymap = [
    [boardLock,backTrack,KC.LEFT,KC.SPACE,KC.RIGHT,skipTrack,None]
]



encoder.pins = (
    (board.D7,board.D8,board.D9)
)


class volumeLockClass(Key):
    def on_press(self, keyboard, key):
        global volume_lock
        volume_lock = not volume_lock
    def on_release(self, keyboard, key):
        pass

volumeLock = volumeLockClass()


class volumeChange(Key):
    def __init__(self,key):
        self.key = key
    def on_press(self, keyboard, key):
        if not volume_lock:
            keyboard.tap_key(self.key)
    def on_release(self, keyboard, key):
        pass

volumeDown = volumeChange(KC.VOLD)
volumeUp = volumeChange(KC.VOLU)


encoder.map = [(
    (volumeDown,volumeUp,volumeLock)
)]


if __name__ == "__main__":
    keyboard.go()
