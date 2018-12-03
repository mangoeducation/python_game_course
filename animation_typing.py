import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

def draw_circle(x):
    arcade.draw_circle_filled(x,300,50,(255,0,0))
    
def draw(x):
    arcade.start_render()
    draw_circle(x)
    #  Finish and run
    arcade.finish_render()

arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT, "hello user")

arcade.set_background_color((0,255,0))

for i in range(90):
    draw(i)

arcade.run()
