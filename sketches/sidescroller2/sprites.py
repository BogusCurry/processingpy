# coding=utf-8

class Sprite(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vely = 0
        self.step = 0
        
    
    def update(self):
        pass
    
    def show(self):
        pass

class Alien(Sprite):
    
    def __init__(self, x, y):
        Sprite.__init__(self, x, y)
        self.status = "walking"
        self.im1 = loadImage("alienwalk1.png")
        self.im2 = loadImage("alienwalk2.png")
        self.im3 = loadImage("alienjump.png")
        self.count = 0

    def update(self):
        if self.status == "jumping":
            self.vely += 0.1
               
    def show(self):
        if self.status == "walking":
            self.count += 1
            if self.count > 15:
                self.count = 0
            if self.count < 8:
                image(self.im1, self.x, self.y)
            else:
                image(self.im2, self.x, self.y)
        elif self.status == "jumping":
            self.y += self.vely
            image(self.im3, self.x, self.y)
            if self.y >= 320:
                self.y = 320
                self.status = "walking"


class Obstacle(Sprite):
    
            def __init__(self, x, y, im):
                Sprite.__init__(self, x, y)
                self.im = loadImage(im + ".png")
                self.step = -4
           
            def update(self):
                self.x += self.step
                if self.x <= -150:
                    self.x = width + 750
            
            def show(self):
                image(self.im, self.x, self.y)    
