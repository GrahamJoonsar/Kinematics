# Inverse Kinematics with two lines
# I didn't feel like figuring out how to do it professionally, so I made my own way of doing it.

import pygame, math



# Window Setup
windowWidth = 1000
windowHeight = 1000
pygame.init()
win = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Pygame window!")

# Other setup code for your program goes here

def distCheck(x1, y1, x2, y2, distance, tolerance):
    return distance * distance - tolerance <= (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) <= distance * distance + tolerance

def dist(x1, y1, x2, y2):
    return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), 10)

n1 = Node (windowWidth/2, windowWidth/2)

l1 = 300
l2 = 300

running = True
cangle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    win.fill((0, 0, 0))

    # Mouse position
    mx, my = pygame.mouse.get_pos()

    # Circle
    pygame.draw.circle(win, (255, 255, 255), (mx, my), 100)
    pygame.draw.circle(win, (0, 0, 0), (mx, my), 99)
    mx = mx + math.cos(cangle) * 100
    my = my + math.sin(cangle) * 100
    cangle += math.pi/360



    if not abs(l1-l2)*abs(l1-l2) < dist(windowWidth/2, windowHeight/2, mx, my) < (l1+l2)*(l1+l2):
        pygame.draw.line(win, (255, 0, 0), (windowWidth/2, windowWidth/2), (mx, my), 5)
    else:
        angle1 = math.atan2(windowWidth/2 - my, windowWidth/2 - mx)

        while not distCheck(math.cos(angle1) * l1 + windowWidth/2, math.sin(angle1) * l1 + windowWidth/2, mx, my, l2, 5000):
            angle1 += 0.001

        a1x = (math.cos(angle1) * l1 + windowWidth/2)
        a1y = (math.sin(angle1) * l1 + windowWidth/2)

        pygame.draw.line(win, (255, 255, 200), (windowWidth/2, windowWidth/2), (a1x, a1y), 2)
        pygame.draw.line(win, (255, 200, 255), (a1x, a1y), (mx, my), 2)

    pygame.display.update()

pygame.quit()
