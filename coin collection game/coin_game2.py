import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COIN_COUNT = 10

class MyGame(arcade.Window):
    """ Our custom Window Class"""
    # Initialization code goes here
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        arcade.set_background_color((255,255,255))
        self.player = None
        self.score = None
        self.set_mouse_visible(False)
        self.player_list = None
        self.coin_list = None
        
    #Basic setup code goes here
    def setup(self):
        self.score = 0
        self.player = arcade.Sprite("character.png",.5)
        self.player.center_x = 50
        self.player.center_y = 50
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)
        self.coin_list = arcade.SpriteList()
        for i in range(COIN_COUNT):
            coin = arcade.Sprite("coin_01.png",.2)
            coin.center_x = random.randrange(0,SCREEN_WIDTH)
            coin.center_y = random.randrange(0,SCREEN_HEIGHT)
            self.coin_list.append(coin)

    #draw code goes here
    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.coin_list.draw()
        if self.score == 5:
            arcade.draw_text("GAME OVER", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, (0,0,0), 20)

    #mouse action code goes here
    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        # Move the center of the sprite to match mouse x, y
        self.player.center_x = x
        self.player.center_y = y

    def update(self, delta_time):
        self.coin_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in hit_list:
            coin.kill()
            self.score = self.score + 1
                

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
