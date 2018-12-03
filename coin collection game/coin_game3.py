import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Coin game")
        self.player = ""
        self.score = ""
        self.coin = ""
        self.set_mouse_visible(False)
        arcade.set_background_color((20,100,0))
        self.coin_list = ""

    def setup(self):
        self.player = arcade.Sprite("character.png",0.5)
        self.player.center_x = 400
        self.player.center_y = 300
        self.coin_list = arcade.SpriteList()
        self.score = 0


        for i in range(10):
            coin = arcade.Sprite("coin_01.png",0.5)
            coin.center_x = random.randrange(0,SCREEN_WIDTH)
            coin.center_y = random.randrange(0,SCREEN_HEIGHT)
            self.coin_list.append(coin)
        
    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.coin_list.draw()
        arcade.draw_text(str(self.score), 10, 20, arcade.color.WHITE, 14)


    def update(self,delta_time):
        hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for obj in hit_list:
            obj.kill()
            self.score = self.score + 1
        print(self.score)
    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        # Move the center of the sprite to match mouse x, y
        self.player.center_x = x
        self.player.center_y = y



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
