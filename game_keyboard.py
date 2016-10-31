import pygame
pygame.init()

#set hight and width of screen
size = [400,400]

#initialise screen or window for dispay
screen = pygame.display.set_mode(size)

#set title of the window
pygame.display.set_caption("Bat and Ball")

#make mouse cursor invisible
pygame.mouse.set_visible(0)

#create bat surface
bat_surf = pygame.Surface((64,12))
#set bat color
bat_surf.fill((0,255,0))
#get rectangular area of bat_surf
batrect = bat_surf.get_rect()
#do similar with ball
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
pygame.key.set_repeat (30,30)
gameScore = 0

while done == 0:
	screen.fill((0,0,0))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=1
		if event.type == pygame.KEYDOWN:
        		if event.key == pygame.K_LEFT:
            			batrect.centerx -= 5
        		if event.key == pygame.K_RIGHT:
            			batrect.centerx += 5
	
	ballrect.left += speed[0]
	ballrect.top += speed[1]

	if ballrect.colliderect(batrect):
		speed[1] = -speed[1]
		gameScore += 1

	if ballrect.left < 0 or ballrect.right > size[0]:
		speed[0] = -speed[0]
	if ballrect.top < 0:
		speed[1] = -speed[1]

	if ballrect.top > size[1]:
		screen.blit(text, textRect)
		pygame.display.flip()
		pygame.time.wait(2000)
		ballrect.top=0; 
		ballrect.left=(size[0]/2)
		gameScore = 0

	screen.blit(ball_surf,ballrect)
	screen.blit(bat_surf,batrect)
	label = font.render(str(gameScore), 1, (255,255,255))
	screen.blit(label, (10, 10))

	clock.tick(100)
	pygame.display.flip()













			

	





