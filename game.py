import pygame
#from pygame.locals import *
pygame.init()

#set hight and width of screen
size = [400,400]

#initialise screen or window for dispay
screen = pygame.display.set_mode(size)

#set title of the window
pygame.display.set_caption("Bat and Ball")

pygame.mouse.set_visible(0)

bat_surf = pygame.Surface((64,12))
bat_surf.fill((0,255,0))
batrect = bat_surf.get_rect()
ball_surf = pygame.Surface((30,30))
ballrect = ball_surf.get_rect()

ball = pygame.draw.circle(ball_surf, (0,0,255),[15,15],15)

speed = [3,3]

batrect.center = ((size[0]/2), (size[1]-50))

font = pygame.font.Font(None, 36)
text = font.render("Game Over",True,(255,0,0))
textRect = text.get_rect()
textRect.centerx = (size[0]/2)
textRect.centery = (size[1]/2)

done =0 
tick_count = 60
clock = pygame.time.Clock()

while done == 0:
	screen.fill((0,0,0))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=1
	
	position = pygame.mouse.get_pos()
	batrect.centerx = position[0]

	ballrect.left += speed[0]
	ballrect.top += speed[1]

	if ballrect.colliderect(batrect):
		speed[1] = -speed[1]

	if ballrect.left < 0 or ballrect.right > size[0]:
		speed[0] = -speed[0]
	if ballrect.top < 0:
		speed[1] = -speed[1]

	if ballrect.top > size[1]:
		screen.blit(text, textRect)
		pygame.display.flip()
		pygame.time.wait(2000)
		tick_count = 60
		ballrect.top=0; ballrect.left=(size[0]/2)

	screen.blit(ball_surf,ballrect)
	screen.blit(bat_surf,batrect)

	clock.tick(tick_count)
	tick_count = tick_count
	pygame.display.flip()













			

	





