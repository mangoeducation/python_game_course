import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        arcade.set_background_color((255,0,0))
        
    def on_draw(self):
        arcade.start_render()


def main():
    """ Main method """
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
