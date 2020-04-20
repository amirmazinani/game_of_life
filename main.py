import os
import time
import random


def clear(): return os.system('clear')


def draw(u, w, h):
    clear()
    for y in range(h):
        for x in range(w):
            if u[y][x]:
                print("O", end="")
            else:
                print(" ", end="")
        print("\n")


def evolution(u, w, h):
    new = [[0 for x in range(w)] for y in range(h)]

    for x in range(w):
        for y in range(h):
            lives = 0
            for xd in range(x-1, x+2):
                for yd in range(y-1, y+2):
                    if u[(yd + h) % h][(xd + w) % w]:
                        lives += 1
            if u[y][x]:
                lives -= 1
            if lives == 3 or (lives == 2 and u[y][x]):
                new[y][x] = 1
            else:
                new[y][x] = 0
    for y in range(h):
        for x in range(w):
            u[y][x] = new[y][x]


if __name__ == "__main__":
    w = 80
    h = 20
    world = [[0 for x in range(w)] for y in range(h)]
    for x in range(w):
        for y in range(h):
            if random.randint(0, 100) % 11 == 0:
                world[y][x] = 1
            else:
                world[y][x] = 0
    while True:
        draw(world, w, h)
        evolution(world, w, h)
        time.sleep(0.3)