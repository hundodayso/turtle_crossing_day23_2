from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.clear()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("black")
        self.show_score()


    def show_score(self):
        self.level += 1
        self.clear()
        self.setpos(-280, 265)
        self.write(f"Level: {self.level}", True, align="left", font=('Courier', 20, 'bold'))

    # def increase_level(self):
    #     self.level
    def game_over(self):
        self.hideturtle()
        self.color("black")
        self.hideturtle()
        self.setpos(0, 0)
        self.write(f"GAME OVER", True, align="center", font=('Courier', 20, 'bold'))
