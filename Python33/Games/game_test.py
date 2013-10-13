#! python3
import os
import pygame
import sys


_image_library = {}
def get_image(path):
    global _image_library

    image = _image_library.get(path)
    if image  == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image


def get_color(color):
    if color == (255, 100, 0):
        return (0, 128, 255)
    else:
        return (255, 100, 0)


def get_positions(x, y, pressed):      
    if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
        x += 3
    if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
        x -= 3
    if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
        y += 3
    if pressed[pygame.K_UP] or pressed[pygame.K_w]:
        y -= 3
    return x, y


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()
    
    x, y, color = 10, 50, (0, 128, 255)
    width, height = 120, 60
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if (event.type == pygame.KEYDOWN and
                   event.key == pygame.K_SPACE):
                color = get_color(color)

        pressed = pygame.key.get_pressed()
        x, y = get_positions(x, y, pressed)

        screen.fill((0, 0, 0))
        screen.blit(get_image('images\silvery.png'), (200, 20))
        pygame.draw.rect(
            screen, color, pygame.Rect(x, y, 120, 60))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
