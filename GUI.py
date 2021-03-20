import pygame
import requests #library for make a call from a site to get a random numbers

WIDTH = 550 #window width
background_color = (251, 247, 245)
original_grid_element_color = (40, 20, 140)
buffer = 5

response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy") # request get a numbers from this site
grid = response.json()['board'] #Here to extract our borad from these response and we will stord it in grid variable
#JavaScript Object Notation (JSON) is a standardized format commonly used to transfer data as text that can be sent over a network

grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

def main():
    pygame.init() #inisiate
    win = pygame.display.set_mode((WIDTH, WIDTH)) #set windows
    pygame.display.set_caption("Sudoku") #name of window
    win.fill(background_color) #background color
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    for i in range(0, 10):
        if (i % 3 == 0): #each 3 line from 0-2 we will draw a sperate bold line that here has size (4)
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2) #vertical lines drawn
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2) #horizntal lines drawn
    pygame.display.update() #a way to display a GUI by pygame library

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if (0 < grid[i][j] < 10):
               value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
               win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()

    while True:
        for event in pygame.event.get():

           if event.type == pygame.QUIT:
                pygame.quit()
                return


main()

