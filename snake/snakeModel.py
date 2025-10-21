from turtle import Turtle, Screen

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
        
        self.turtleSegments[0].forward(20)