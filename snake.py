import curses
from random import randint

# Initialize the screen
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0) 
win.border(0)
win.timeout(100)

#default snake coordniatres
snake_x = 15
snake_y = 10
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]
food = [randint(1, 18), randint(1, 58)]  #randomize it
win.addch(food[0], food[1], '*') #show the food a *

#game logic variables
key = curses.KEY_RIGHT
score = 0

# Game loop
while True:
    next_key = win.getch()
    key = key if next_key == -1 else next_key

    #arrow keys to move
    if key == curses.KEY_DOWN:
        new_head = [snake[0][0] + 1, snake[0][1]]
    elif key == curses.KEY_UP:
        new_head = [snake[0][0] - 1, snake[0][1]]
    elif key == curses.KEY_LEFT:
        new_head = [snake[0][0], snake[0][1] - 1]
    elif key == curses.KEY_RIGHT:
        new_head = [snake[0][0], snake[0][1] + 1]

    #check if the snake dies
    if (
        new_head[0] == 0 or new_head[0] == 19 or
        new_head[1] == 0 or new_head[1] == 59 or
        new_head in snake
    ):
        break


    snake.insert(0, new_head)

    #check if the snake found food
    if snake[0] == food:
        score += 1
        food = None
        while food is None:
            #place new foods
            nf = [
                randint(1, 18),
                randint(1, 58)
            ]
            food = nf if nf not in snake else None
        win.addch(food[0], food[1], '*')
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    win.addch(snake[0][0], snake[0][1], '#')


#end the game
curses.endwin()
print("Game Over! Your score was " + str(score))
