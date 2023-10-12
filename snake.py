from turtle import Turtle

STARTING_POS = [(0, 0), (-11.5, 0), (-22.5, 0)]
MOVE_CONS = 11
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """ini adalah class untuk membuat snake dan menjalankan snake"""

    def __init__(self):
        self.seg_snake = []
        self.create_snake()
        self.head = self.seg_snake[0]

    def create_snake(self):
        # TODO 1 : buat snake muncul pada layar
        for position in STARTING_POS:
            self.add_snake_part(position)

    def add_snake_part(self, position_seg_add):
        """penambahan segmen snake jika memakan food"""
        snake = Turtle("square")
        snake.color("white")
        snake.shapesize(0.5)
        snake.penup()
        snake.goto(position_seg_add)
        self.seg_snake.append(snake)

    def reset_snake(self):
        for seg in self.seg_snake:
            seg.goto(1000, 1000)
        self.seg_snake.clear()
        self.create_snake()
        self.head = self.seg_snake[0]

    def extend(self):
        self.add_snake_part(self.seg_snake[-1].position())  # .position() adalah function dari turtle

    def move(self):
        # TODO 3 : memastikan bahwa ekornya tetap mengikuti kepala saat maju atau belok
        for seg in range(len(self.seg_snake) - 1, 0, -1):
            # membalikkan pergerakan segment turtle, dari array belakang ke depan.
            x_pos = self.seg_snake[seg - 1].xcor()
            y_pos = self.seg_snake[seg - 1].ycor()
            self.seg_snake[seg].goto(x_pos, y_pos)
        self.head.forward(MOVE_CONS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
