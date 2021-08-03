import pygame
pygame.mixer.init()
pygame.mixer.music.load("./DataFiles/EmployeeAudio/1.ogg")
pygame.mixer.music.queue("./DataFiles/EmployeeAudio/Success.ogg")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()

while True:
	
	print("Press 'p' to pause, 'r' to resume")
	print("Press 'e' to exit the program")
	query = input(" ")
	
	if query == 'p':

		# Pausing the music
		pygame.mixer.music.pause()	
	elif query == 'r':

		# Resuming the music
		pygame.mixer.music.unpause()
	elif query == 'e':

		# Stop the mixer
		pygame.mixer.music.stop()
		break