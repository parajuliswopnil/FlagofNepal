import pygame
import sys
from pygame.locals import QUIT
import pygame.gfxdraw

#pygame initiation

pygame.init()

#screen resolution calculation
screen_resolution = pygame.display.Info()
print(screen_resolution.current_h)
print(screen_resolution.current_w)
print(f"Screen Resolution : {screen_resolution.current_w} x {screen_resolution.current_h}")

#setting the field for drawing the flag

drawingSurface = pygame.display.set_mode((900, 900))
pygame.display.set_caption("My Nepal My Pride")

#all the colors required
colorBlack = (0,0,0)
colorWhite = (255,255,255)
colorRed = (255,0,0)
colorBlue = (0,0,255)
colorTeal = (0,128,128)

#filling the drawing surface with teal

drawingSurface.fill(colorTeal)

#giving the shape of the flag in blue first

pygame.draw.polygon(drawingSurface,colorBlue,((229,9),(629,309),(404,309),(629,609),(229,609)))

#overlapping the blue with red
pygame.gfxdraw.filled_polygon(drawingSurface,((239,29),(604,302),(385,299),(610,599),(239,599)), colorRed)

#function to make star done by overlapping 4 triangles on top of one another

def star(cx,cy,s): #s is the scaling factor to make the smaller half star in the moon section
    pygame.draw.polygon(drawingSurface, colorWhite, [[361*s + cx, 386*s + cy], [415*s + cx, 479*s + cy], [309*s + cx, 479*s + cy]])
    pygame.draw.polygon(drawingSurface, colorWhite, [[361*s + cx, 509*s + cy], [310*s + cx, 416*s + cy], [414*s + cx, 416*s + cy]])
    pygame.draw.polygon(drawingSurface, colorWhite, [[300*s + cx, 447*s + cy], [393*s + cx, 395*s + cy], [392*s + cx, 500*s + cy]])
    pygame.draw.polygon(drawingSurface, colorWhite, [[424*s + cx, 448*s + cy], [331*s + cx, 500*s + cy], [330*s + cx, 395*s + cy]])

star(-20,-10,1)

#making a crecent moon by making a white circle and stacking it with a red circle

pygame.draw.circle(drawingSurface,colorWhite,(335,190),57)
pygame.draw.circle(drawingSurface,colorRed,(335,170),57)
star(120,-59,0.6)


#updating the figure

pygame.display.update()

#so that the event doesnot disapper implicitly

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
