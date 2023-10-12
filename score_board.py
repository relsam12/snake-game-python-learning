from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 13, 'normal')



class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        # Metode untuk mebuka dan membaca file text yang menyimpan highscore
        with open("high_score_library.txt", mode="r") as hsl:
            self.high_score = int(hsl.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Metode untuk menyimpan data highscore dan akan ditampilkan dari pencapaian sebelumnya
            with open("high_score_library.txt", mode="w") as hsl:
                hsl.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER !!!", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()
