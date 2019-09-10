'''
Instructions:
1) Review and run the 0_2_drawing_primitives.py file and investigate how the different shapes, text, and images
are drawn to the screen.

2) In this file, try to use the different arcade commands to draw your favourite emoji.  You should explore
* drawing filled shapes
* drawing shape outlines
* drawing text
'''


import arcade
import os

# change the window dimensions if you need to
arcade.open_window(600, 600, "My Emoji Attempt")


arcade.set_background_color(arcade.color.WHITE)


arcade.start_render()

# place all your drawing commands in between the start_render() and finish_render() commands

arcade.finish_render()


arcade.run()
