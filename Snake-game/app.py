import random
import curses  # shape of snake

screen = curses.initscr()
curses.curs_set(0) # hide the mouse

screen_height , screen_widght = screen.getmaxyx()
window = curses.newwin(screen_height , screen_widght , 0 , 0) # create a new window

window.keypad(1) # receive input from keyboard
window.timeout(115) # delay for updating the screen

# initial postion of snake head
snk_x = screen_widght // 4
snk_y = screen_height // 2

# initial postion of snake body
snake = [
    [snk_y , snk_x], # Head
    [snk_y , snk_x-1], # body
    [snk_y , snk_x-2] # tail
]

food = [screen_height // 2 , screen_widght // 2] # create the food in the middle of the window

window.addch(food[0] , food[1] , curses.ACS_PI) # character of food

key = curses.KEY_RIGHT # intial movement 

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    # snake collided with the wall or itself
    if snake[0][0] in [0 , screen_height] or snake[0][1] in [0 , screen_widght] or snake[0] in snake[1 : ]:
        curses.endwin() # closing the window
        quit() # exit the program
    
    new_head = [snake[0][0] , snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    
    snake.insert(0 , new_head)

    # snake eat food 
    if snake[0] == food:
        food = None # remove the food
        # new food in the random place
        while food == None:
            new_food = [
                random.randint(1 , screen_height - 1),
                random.randint(1 , screen_widght - 1)
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0] , food[1] , curses.ACS_PI)
    # remove the last segment of snake body
    else:
        tail = snake.pop()
        window.addch(tail[0] , tail[1] , ' ')
    
    # appear the snake on the screen 
    window.addch(snake[0][0] , snake[0][1] , curses.ACS_CKBOARD)
