from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

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

snake = Snake()
food = Food()
sb = ScoreBoard()

# establishing event listeners so snake can be controlled
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# animating the snake segments on screen
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        sb.increment_score()
        sb.update_scoreboard()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        sb.game_over()




screen.exitonclick()

