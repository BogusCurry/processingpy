p = 2
f = 1
MAXITER = 60000

def setup():
    size(600, 600)
    this.surface.setTitle("Primzahl-Spirale")
    background(51)
    frameRate(1000)
        
def draw():
    global p, f, i
    translate(width/2, height/2)
    noStroke()
    fill(0, 200, 0)
    # Sieb des Eratosthenes
    if f%p%2:
        x = p*sin(p)*0.005
        y = p*cos(p)*0.005
        ellipse(x, y, 2, 2)
    p += 1
    f *= (p-2)
    if p > MAXITER:
        print("I did it, Babe!")
        noLoop()    
        
        
