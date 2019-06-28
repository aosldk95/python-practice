import audio
import keyboard
import gamecon

class gameeng:

    def _init_(self):
        self.keyboard=keyboard.keyboard()
        self.gamecon=gamecon.gamecon()

    def start(self):
        audio.getobj.start()
        self.gamecon.start()