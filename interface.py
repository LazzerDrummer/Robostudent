# import math
import os
import pygame


pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
blue = (128, 212, 255)


class Board:

    def __init__(self, player, side, tiles_number):
        self.spaces = [0]*pow(tiles_number, 2)
        self.player = player
        self.side = side
        self.tiles_number = tiles_number
        self.division = side/tiles_number
        self.size = [side, side]
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Frozen Lake')
        self.window.fill(blue)

    def draw_board(self, line_width):
        start_correction = 1
        end_correction = 2
        if line_width == 1:
            start_correction = 0
            end_correction = 0
        elif line_width == 2:
            start_correction = 0
            end_correction = 1
        elif line_width % 2 == 0:
            start_correction = 1
            end_correction = 3
        rectangle = [start_correction, start_correction, self.side -
                     end_correction, self.side - end_correction]
        pygame.draw.rect(self.window, black, rectangle, line_width)
        for i in range(1, self.tiles_number):
            pygame.draw.line(self.window, black, [self.division*i, 0], [
                self.division*i, self.side], line_width)
            pygame.draw.line(self.window, black, [0, self.division*i], [
                self.side, self.division*i], line_width)


def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # frames = 60
    board = Board(0, 500, 3)

    done = False
    clock = pygame.time.Clock()

    while not done:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        board.draw_board(3)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
