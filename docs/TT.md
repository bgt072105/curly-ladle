{% include navigation.html %}

## GitHub Acitivites
[Major Commit (on GitHub)](https://github.com/bgt072105/curly-ladle/commit/76c23152314b69f9234e98475552dedd69916de0)

[Code on Replit](https://replit.com/join/shwebjagoo-bgt072105)

Key Takeaways:
* I learned how to implement menus and submenus
* I learned how to call functions through the use of menus

```
main_menu = [
    ["swapNumbers", swapNumbers.swapnumbers],
    ["matrix", matrix.keypad],
]

sub_menu = [
    ["Tree", tree.tree],
    ["Funcy", funcy.person],
]
```
```
def person_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "  \ O / ")
    print(sp + "   \|/  ")
    # print(SHIP_COLOR, end="")
    print(sp + "    | ")
    print(sp + "   / \  ")
    print(sp + "  /   \  ")
    print(RESET_COLOR)
 ```