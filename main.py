import os
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