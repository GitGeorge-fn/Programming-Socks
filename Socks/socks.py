import pygame

# constant variables


Screen_Size = (700,500)
Light_Green = (52,235,70)

#init

pygame.init()

screen = pygame.display.set_mode(Screen_Size)
pygame.display.set_caption('Sock Hunter')

while True:
# game loop

	#input
	for event in pygame.event.get():
		print(event)

	#update

	#draw

	screen.fill(Light_Green)
	pygame.display.flip()
#quit

pygame.quit()

