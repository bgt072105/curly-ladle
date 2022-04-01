
#funcy.py
import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
RESET_COLOR = u"\u001B[0m\u001B[2D"

# print ship with colors and leading spaces
def wave():
    time.sleep(.5)
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    print("  \ O / ")
    print("   \|/  ")
    print("    | ")
    print("   / \  ")
    print("  /   \  ")
    print(RESET_COLOR)
    time.sleep(.5)
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    print("  \ O    ")
    print("   \|___ ")
    print("    |    ")
    print("   / \   ")
    print("  /   \  ")
    print(RESET_COLOR)
    time.sleep(.5)
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    print("  \ O   ")
    print("   \|   ")
    print("    |\  ")
    print("   / \\\ ")
    print("  /   \  ")
    print(RESET_COLOR)
    time.sleep(.5)
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    print("  \ O    ")
    print("   \|___   ")
    print("    |    ")
    print("   / \   ")
    print("  /   \  ")
    print(RESET_COLOR)
    time.sleep(.5)
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    print("  \ O /  ")
    print("   \|/   ")
    print("    |   ")
    print("   / \  ")
    print("  /   \  ")
    print(RESET_COLOR)
    time.sleep(.5)