# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
# import loopy
# import mathpy
from week0 import tree
from week0 import funcy
from week0 import swapNumbers
from week0 import matrix
# import patterns
from week1 import info
from week1 import fibonacci
from week1 import factorial
from week2 import factorial2
from week2 import gcdOOP
from week2 import gcdImperative

main_menu = [
]

sub_menu_animations = [
    ["Tree", tree.tree],
    ["Funcy", funcy.person],
]

sub_menu_math = [
    ["swapNumbers", swapNumbers.swapnumbers],
    ["fibonacci", fibonacci.fib_tester],
    ["factorialClass", factorial2.fac2_tester],
    ["factorial", factorial.fac_tester],
    ["gcdOOP", gcdOOP.GCD_OOP_tester],
    ["gcdImperative", gcdImperative.GCD_Imperative_tester]
]

sub_menu_data = [
    ["matrix", matrix.keypad],
    ["info", info.infoDB],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["data", submenu_data])
    menu_list.append(["math", submenu_math])
    menu_list.append(["animations", submenu_animations])
    buildMenu(title, menu_list)


def submenu_data():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu_data)

def submenu_math():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu_math)

def submenu_animations():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu_animations)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
