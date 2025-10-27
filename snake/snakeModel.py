from turtle import Turtle, Screen
DISTANCE = 20
RIGHT = 0
DOWN = 90
LEFT = 180
UP = 270

class Snake:
    def __init__(self, startingLocations):
        self.turtleSegments = []
        self.startingLocations = startingLocations
        self.create_snake()
        self.head = self.turtleSegments[0]

    def create_snake(self):
        for pos in self.startingLocations:
            self.add_segment(pos)
    
    def add_segment(self, pos):
        t = Turtle('square')
        t.color('white')
        t.penup()
        t.goto(pos)
        self.turtleSegments.append(t)
        return t
    
    def extend(self):
        self.add_segment(self.turtleSegments[-1].position())

    def move(self):
        for tSegNum in range(len(self.turtleSegments)-1, 0, -1): 
            newX = self.turtleSegments[tSegNum-1].xcor()
            newY = self.turtleSegments[tSegNum-1].ycor()
            self.turtleSegments[tSegNum].goto(newX, newY)
        
        self.turtleSegments[0].forward(DISTANCE)
    
    def reset(self):
        for tseg in self.turtleSegments:
            tseg.goto((2000,2000))
        self.turtleSegments.clear()
        self.create_snake()
        self.head = self.turtleSegments[0]

    
    def right(self):
        if self.turtleSegments[0].heading() != RIGHT and self.turtleSegments[0].heading() != LEFT:
            self.turtleSegments[0].setheading(RIGHT)

    def up(self):
        if self.turtleSegments[0].heading() != DOWN and self.turtleSegments[0].heading() != UP:
            self.turtleSegments[0].setheading(DOWN)

    def left(self):
        if self.turtleSegments[0].heading() != LEFT and self.turtleSegments[0].heading() != RIGHT:
            self.turtleSegments[0].setheading(LEFT)

    def down(self):
        if self.turtleSegments[0].heading() != UP and self.turtleSegments[0].heading() != DOWN:
            self.turtleSegments[0].setheading(UP)