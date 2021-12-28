from turtle import Turtle, Screen
import time

# 1. create a snake body
# 2. Move the snake
# 3. Control the Snake using keyboard controls
# 4. detect collision with food
# 5. create a scoreboard
# 6. detect collision with wall
# 7. detect collision with tail

# creating screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# creating snake body + starting positions
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# animating the snake segments on screen
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    for seg_num in range(len(segments)-1, 0, -1):
        segments[seg_num].goto(segments[seg_num-1].xcor(), segments[seg_num-1].ycor())
    segments[0].forward(20)










screen.exitonclick()

