import random
from game import constants
from game.action import Action
from game.point import Point
import sys
class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        i = 0
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0] # there's only one
        bricks = cast["brick"]
        #this checks if bricks are hit by the ball, and from what direction the ball comes from, reversing the velocity
        #based on a diagonal hit or vertical hit
        for brick in bricks:
            #this checks if the ball hits from the front
            if ball.get_position().equals(brick.get_position()):
                y = -ball.get_velocity().get_y()
                x = ball.get_velocity().get_x()
                new_velocity = Point(x,y)
                ball.set_velocity(new_velocity)
                bricks.pop(i)
                break
            #this checks if the ball hits from the side
            elif ball.get_velocity().get_x() != 0 and ball.get_velocity().get_y() != 0:
                if (brick.get_position().get_x() + ball.get_velocity().get_x()) == ball.get_position().get_x() and brick.get_position().get_y() == ball.get_position().get_y():
                    y = -ball.get_velocity().get_y()
                    x = -ball.get_velocity().get_x()
                    new_velocity = Point(x,y)
                    ball.set_velocity(new_velocity)
                    bricks.pop(i)
                    break

            i += 1
        #this for statement replicates the location of the paddle and its 10 character length, 
        # so that the user can bounce the ball off of the paddle
        for i in range(0,10):
            if paddle.get_position().get_x()+i == ball.get_position().get_x():
                if ball.get_position().get_y() == constants.MAX_Y-2:
                    y = -ball.get_velocity().get_y()
                    x = ball.get_velocity().get_x()
                    new_velocity = Point(x,y)
                    ball.set_velocity(new_velocity)
            #exit the game if the ball hits the floor and loses
            elif ball.get_position().get_y() == constants.MAX_Y-1:
                print("you lost")
                sys.exit()
            
        #this checks if the ball hits the ceiling
        if ball.get_position().get_y() == 1:
            y = -ball.get_velocity().get_y()
            x = ball.get_velocity().get_x()
            new_velocity = Point(x,y)
            ball.set_velocity(new_velocity)
        #this checks if the ball hits the walls
        if ball.get_position().get_x() == 1 or ball.get_position().get_x() == constants.MAX_X-1:
            y = ball.get_velocity().get_y()
            x = -ball.get_velocity().get_x()
            new_velocity = Point(x,y)
            ball.set_velocity(new_velocity)
        