
import arcade

# open a window. length, width, name of the window are the parameters
arcade.open_window(600,600,"my first window")

# set the background of the window
arcade.set_background_color((255,0,0))

#start and close render
arcade.start_render()

arcade.draw_rectangle_filled(300,300,100,10,(255,255,0),80)
arcade.draw_circle_filled(0,300,50,(255,120,52))
arcade.finish_render()

#this line is needed for the window keep running
arcade.run()
