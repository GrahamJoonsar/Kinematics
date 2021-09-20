# Inverse Kinematics with two lines
# I didn't feel like figuring out how to do it professionally, so I made my own way of doing it.

import pygame, math



# Window Setup
windowWidth = 1000
windowHeight = 1000
pygame.init()
win = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Pygame window!")

cangle = 0
circle = False

# Other setup code for your program goes here

def distCheck(x1, y1, x2, y2, distance, tolerance):
    return distance * distance - tolerance <= (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) <= distance * distance + tolerance

def dist(x1, y1, x2, y2):
    return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)

class DoubleKinematic:
    def __init__(self, x, y, l1, l2):
        self.x = x
        self.y = y
        self.l1 = l1
        self.l2 = l2
    
    def draw(self):
        global cangle
        mx, my = pygame.mouse.get_pos()

        # Circle
        if circle:
            mx = mx + math.cos(cangle) * 100
            my = my + math.sin(cangle) * 100
            cangle += math.pi/360

        if not abs(self.l1-self.l2)*abs(self.l1-self.l2) < dist(self.x, self.y, mx, my) < (self.l1+self.l2)*(self.l1+self.l2):
            pygame.draw.line(win, (255, 0, 0), (self.x, self.y), (mx, my), 5)
        else:
            angle1 = math.atan2(self.y - my, self.x - mx)

            while not distCheck(math.cos(angle1) * self.l1 + self.x, math.sin(angle1) * self.l1 + self.y, mx, my, self.l2, 5000):
                angle1 += 0.01

            a1x = (math.cos(angle1) * self.l1 + self.x)
            a1y = (math.sin(angle1) * self.l1 + self.y)

            pygame.draw.line(win, (255, 255, 200), (self.x, self.y), (a1x, a1y), 2)
            pygame.draw.line(win, (255, 200, 255), (a1x, a1y), (mx, my), 2)

dks = []

dksSide = 2

for i in range(dksSide):
    for j in range(dksSide):
        dks.append(DoubleKinematic((j-(dksSide/2))*50 + windowWidth/2, (i-(dksSide/2))*50 + windowHeight/2, 300, 300))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    win.fill((0, 0, 0))
    mx, my = pygame.mouse.get_pos()

    # Circle
    if circle:
        pygame.draw.circle(win, (255, 255, 255), (mx, my), 100)
        pygame.draw.circle(win, (0, 0, 0), (mx, my), 99)

    # Mouse position
    #mx, my = pygame.mouse.get_pos()

    # Circle
    #pygame.draw.circle(win, (255, 255, 255), (mx, my), 100)
    #pygame.draw.circle(win, (0, 0, 0), (mx, my), 99)
    #mx = mx + math.cos(cangle) * 100
    #my = my + math.sin(cangle) * 100
    #cangle += math.pi/360

    for dk in dks:
        dk.draw()

    pygame.display.update()

pygame.quit()
