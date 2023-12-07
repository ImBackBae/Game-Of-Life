import pygame
import random
import time
import ctypes
import os
import keyboard

def next_gen(cells):
    coord_zero = []
    coord_one = []
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            count = neighbours_count(cells, i, j)
            if cells[i][j] == 1:
                if count < 2:
                    coord_zero.append((i, j))
                elif count > 3:
                    coord_zero.append((i, j))
            elif cells[i][j] == 0:
                if count == 3:
                    coord_one.append((i, j))
    for i in coord_zero:
        cells[i[0]][i[1]] = 0
    
    for i in coord_one:
        cells[i[0]][i[1]] = 1
        
    return cells
def neighbours_count(cells, i, j):
    count = 0
    if i + 1 < len(cells) and cells[i+1][j] == 1:
        count += 1

    if i - 1 >= 0 and cells[i-1][j] == 1:
        count += 1

    if j - 1 >= 0 and cells[i][j-1] == 1:
        count += 1

    if j + 1 < len(cells[i]) and cells[i][j+1] == 1:
        count += 1
    
    if i - 1 >= 0 and  j - 1 >= 0 and cells[i-1][j-1] == 1:
        count += 1
    
    if i - 1 >= 0 and  j + 1 < len(cells[i]) and cells[i-1][j+1] == 1:
        count += 1
    
    if i + 1 < len(cells) and  j - 1 >= 0 and cells[i+1][j-1] == 1:
        count += 1
    
    if i + 1 < len(cells) and j + 1 < len(cells[i]) and cells[i+1][j+1] == 1:
        count += 1
    
    return count
def create_cell(width, height, side):
	cells = []
	for i in range(width//side):
		cells.append([])
		for j in range(height//side):
			cells[i].append(random.randint(0,1))
	return cells
def main():
	pygame.init()
	side = 10
	WHITE = (255,255,255)
	BLACK = (0,0,0)
	screen = pygame.display.set_mode((1280,800))

	cells = create_cell(1280, 800, side)
	running = True
	pause = False

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		if keyboard.is_pressed("r"):
			cells = create_cell(1280, 800, side)
		if keyboard.is_pressed("p"):
			if pause == False:
				pause = True
			else:
				pause = False

		for i in range(len(cells)):
			for j in range(len(cells[i])):
				if cells[i][j] == 1:
					pygame.draw.rect(screen, WHITE, (side*i,side*j,side-1,side-1))
				elif cells[i][j] == 0:
					pygame.draw.rect(screen, BLACK, (side*i,side*j,side,side))
		# pygame.image.save(screen,"screenshot.jpg")
		# ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath("screenshot.jpg") , 0)
		time.sleep(0.1)
		if pause == False:
			next_gen(cells)
		else:
			pass
		pygame.display.flip()

main()