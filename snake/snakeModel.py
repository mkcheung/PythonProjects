from turtle import Turtle, Screen
DISTANCE = 20
RIGHT = 0
DOWN = 90
LEFT = 180
UP = 270

class Snake:
    def __init__(self, startingLocations):
        self.turtleSegments = []
        for pos in startingLocations:
            t = Turtle('square')
            t.color('white')
            t.penup()
            t.goto(pos)
            self.turtleSegments.append(t)

    def move(self):
        for tSegNum in range(len(self.turtleSegments)-1, 0, -1): 
            newX = self.turtleSegments[tSegNum-1].xcor()
            newY = self.turtleSegments[tSegNum-1].ycor()
            self.turtleSegments[tSegNum].goto(newX, newY)
        
        self.turtleSegments[0].forward(DISTANCE)

    
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

    def head(self):
        return self.turtleSegments[0]