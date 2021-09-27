import pygame, math

# Window Setup
windowWidth = 750
windowHeight = 750
tolerance = 5
pygame.init()
win = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Pygame window!")

def dist(x1, y1, x2, y2, val):
    return val*val - tolerance <= (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) <= val*val + tolerance

# Other setup code for your program goes here
class Segment:
    def __init__(self, len):
        self.len = len
        self.angle = math.pi/4
        self.x = 0
        self.y = 0
    def draw(self):
        pygame.draw.line(win, (255, 255, 255), (self.x, self.y), (math.cos(self.angle) * self.len + self.x, math.sin(self.angle) * self.len + self.y), 2)
    def getNextPosX(self):
        return math.cos(self.angle) * self.len + self.x
    def getNextPosY(self):
        return math.sin(self.angle) * self.len + self.y


segments = [Segment(50), Segment(50), Segment(50), Segment(50), Segment(50), Segment(50), Segment(50), Segment(50), Segment(50), Segment(50)]

segments[0].x = windowWidth/2
segments[0].y = windowHeight/2

def getRestOfDist(i):
    temp = 0
    for j in range(i+1, len(segments)):
        temp += segments[j].len
    return temp


distTolerance = 8000

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((0, 0, 0))

    mx, my = pygame.mouse.get_pos()

    for i in range(len(segments)):
        segments[i].draw()
        check = 0
        while not dist(segments[i].getNextPosX(), segments[i].getNextPosY(), mx, my, getRestOfDist(i)) and check <= distTolerance*2:
            if len(segments)/2 < i:
                segments[i].angle += math.pi/(distTolerance)
            else:
                segments[i].angle -= math.pi/(distTolerance)
            check += 1

        if i < len(segments)-1:
            segments[i+1].x = math.cos(segments[i].angle) * segments[i].len + segments[i].x
            segments[i+1].y = math.sin(segments[i].angle) * segments[i].len + segments[i].y



    pygame.display.update()

pygame.quit()
