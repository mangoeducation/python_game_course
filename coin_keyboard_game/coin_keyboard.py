import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Coin game with Mouse")
        self.player = None
        self.coinList = None
        self.score = None
        arcade.set_background_color((255,200,200))

    def setup(self):
        self.player = arcade.Sprite("character.png",1)
        self.player.center_x = 200
        self.player.center_y = 200
        self.coinList = arcade.SpriteList()
        self.score = 0

        
    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def 

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
