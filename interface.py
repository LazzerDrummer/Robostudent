# import math
import os
import pygame


pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)


class Board:

    def __init__(self, player, side):
        self.spaces = [0]*9
        self.player = player
        self.side = side
        self.division = side/3
        self.size = [side, side]
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Tic Tac Toe')
        self.window.fill(grey)

    def show_board(self):
        pygame.draw.line(self.window, black, [self.division, 0], [
                         self.division, self.side], 1)
        pygame.draw.line(self.window, black, [self.division*2, 0], [
                         self.division*2, self.side], 1)
        pygame.draw.line(self.window, black, [0, self.division], [
                         self.side, self.division], 1)
        pygame.draw.line(self.window, black, [0, self.division*2], [
                         self.side, self.division*2], 1)


def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    frames = 60
    board = Board(0, 500)

    done = False
    clock = pygame.time.Clock()

    while not done:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        board.show_board()
        # window.fill(grey)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
