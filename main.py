import pygame,sys

#def

def bouncing_rect():

	global x_speed,y_speed

	moving_rect.x += x_speed
	moving_rect.y += y_speed

	pygame.draw.rect(screen, color_white, moving_rect)  # draw white
	pygame.draw.rect(screen, color_red, other_rect)  # draw red

	#collison with screen borders
	if moving_rect.right>+ screen_width or moving_rect.left <=0:
		x_speed *=-1
	if moving_rect.bottom>+ screen_height or moving_rect.top <=0:
		y_speed *=-1



# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 800
screen_height =800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Surfaces and Rectangles collisions")
color_white=(255,255,255)
color_red=(255,0,0)


# Creating the sprites and groups
moving_rect=pygame.Rect(350,350,100,100)
x_speed,y_speed =5,4

other_rect=pygame.Rect(300,600,200,100)
other_speed=2


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		#if event.type == pygame.MOUSEBUTTONDOWN:# on mouse click
			#player.animate()
	# Drawing
	screen.fill((30,30,30)) #grey

	bouncing_rect()


	pygame.display.flip()
	clock.tick(60)
