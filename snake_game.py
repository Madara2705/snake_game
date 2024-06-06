from turtle import Turtle
starting_position = [(0,0), (-20,0), (-40,0)]
move_distance = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN =270

class Snake :

    def __init__(self):
        self.all_snakes = []
        self.create_snake()
    
    def create_snake(self) :
        for position in starting_position :
            self.new_snake(position)

    def new_snake(self, position) :
        snake_body = Turtle()
        snake_body.shape("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.all_snakes.append(snake_body)

    def extend(self) :
        self.new_snake(self.all_snakes[-1].position())

    def snake_move(self) :
        for segment_number in range(len(self.all_snakes) -1 , 0 , -1 ) :
            new_x = self.all_snakes[segment_number - 1].xcor()
            new_y = self.all_snakes[segment_number - 1].ycor()
            self.all_snakes[segment_number].goto(new_x, new_y)
        self.all_snakes[0].forward(move_distance)

    def up(self) :
        if self.all_snakes[0].heading() != DOWN :
            self.all_snakes[0].setheading(UP)

    def down(self) :
        if self.all_snakes[0].heading() != UP :
            self.all_snakes[0].setheading(DOWN)

    def right(self) :
        if self.all_snakes[0].heading() != LEFT :
            self.all_snakes[0].setheading(RIGHT)

    def left(self) :
        if self.all_snakes[0].heading() != RIGHT :
            self.all_snakes[0].setheading(LEFT)



















