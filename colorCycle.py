class ColorCycler:
    def __init__(self, r = 255, g = 255, b = 255):
        self.r = r
        self.g = g
        self.b = b
        self.flag = True

    def cycle(self, backgroundObj):
        if(self.flag):
            if(self.r>150):
                self.r-=1
            elif(self.g>150):
                self.g-=1
            elif(self.b>150):
                self.b-=1
            else:
                self.flag = False
        else:
            if(self.r<255):
                self.r+=1
            elif(self.g<255):
                self.g+=1
            elif(self.b<255):
                self.b+=1
            else:
                self.flag = True

        backgroundObj.fill((self.r,self.g,self.b))
