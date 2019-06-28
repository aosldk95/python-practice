class keyboard:
    def _init_(self):
        self.onkeydown=None
        self.onkeyup=None
    def setonkeydown(self,value):
        self.onkeydown=value
    def setonkeyup(self,value):
        self.onkeyup=value