import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import tkinter as tk


def start_game():
    screen = Screen()
    turtle.TurtleScreen._RUNNING = True
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # Setting the hotkeys
    screen.listen()
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.down, "Down")

    # Moving the snake
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        # Detecting collision with food
        if snake.head.distance(food) < 15:
            scoreboard.counter()
            food.refresh()
            snake.extend()

        # Detecting collision with the wall
        if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            game_on = False
            scoreboard.game_over()


        # Detecting collision with itself
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                game_on = False
                scoreboard.game_over()

    screen.exitonclick()

def quit_game():
    root.destroy()


root = tk.Tk()
root.title("Snake Game")
root.config(padx=100, pady=50, bg="#03d3fc")

# Create a label widget for the title
title_label = tk.Label(root, text="Snake Game", font=("System", 34, "bold"), bg="#03d3fc")
title_label.grid(column=1, row=0, rowspan=2)


# Create the buttons
start_button = tk.Button(text="Start Game", font=("System", 18), command=start_game, bg="#6d5cbf")
start_button.grid(column=1, row=2, sticky="EW", padx=10, pady=10)

quit_button = tk.Button( text="Quit", font=("System", 18), command=quit_game, bg="#6d5cbf")
quit_button.grid(column=1, row=3, sticky="EW", padx=10, pady=10)

root.mainloop()

