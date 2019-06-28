class audio:
    instance= None
    @classmethod
    def getobj(cls):
        if audio.instance==None:
            audio.instance=audio()
    def start(self):
        pass
        return audio.instance
    def play(self,filename):
        print("playing",filename)
