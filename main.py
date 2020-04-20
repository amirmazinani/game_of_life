import os


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