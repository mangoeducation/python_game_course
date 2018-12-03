import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCALE_PLAYER = 0.5
SCALE_COIN = 0.1
COIN_COUNT = 5
class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")
        self.player_list = None
        self.coin_list = None

        self.player = None
        self.score = None
        arcade.set_background_color((255,0,0))

    def setup():
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.player = arcade.Sprite("character.png",SCALE_PLAYER)
        self.score = 0

        self.player_list.append(self.player)
        for i in range(COIN_COUNT):
            coin = arcade.Sprite("coin.png",SCALE_COIN)
    def on_draw(self):
        arcade.start_render()



def main():
    """ Main method """
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
