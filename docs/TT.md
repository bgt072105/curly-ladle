{% include navigation.html %}

## GitHub Acitivites

## Replit Runtime

<iframe height="1000px" width="800px" src="https://replit.com/@bgt072105/curly-ladle?lite=true#main.py"></iframe>

### Week 1
[Major Commit (on GitHub)](https://github.com/bgt072105/curly-ladle/commit/421a528084577742ca3caa54ae8882048602d509)

[Code on Replit](https://replit.com/join/shwebjagoo-bgt072105)

Key Takeaways:
* I practiced using lists within other lists
* I also practiced the logic for fibonaccia

```
InfoDb.append({
    "FirstName": "Brian",
    "LastName": "Tang",
    "FavoriteSport": "Tennis",
    "FavoriteColor": "Blue",
    "FavoriteAnimal": "Dog",
    "CountriesYouWantToTravelTo":["Germany", "Sweden", "United Kingdom", "Poland", "Iceland"]
```
```
def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recur_fibonacci(n-1) + recur_fibonacci(n-2)

def fib_tester():
    try:
        num = int(input("Enter a number for fibonacci: "))
        if num == 0:
            print("invalid")
        else:
            print("Fibonacci Sequence:")
            for i in range(num):
                print(recur_fibonacci(i))
    except ValueError:
        print("invalid")
```

### Week 0
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
