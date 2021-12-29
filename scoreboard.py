from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.sety(270)
        self.write(arg="Score: " + str(self.score), move=False, align='center', font=('Courier', 20, 'normal'))
        self.update_scoreboard()

    def increment_score(self):
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(arg="Score: " + str(self.score), move=False, align='center', font=('Courier', 20, 'normal'))

    def game_over(self):
        self.sety(0)
        self.write(arg="GAME OVER.", move=False, align='center', font=('Courier', 30, 'normal'))




