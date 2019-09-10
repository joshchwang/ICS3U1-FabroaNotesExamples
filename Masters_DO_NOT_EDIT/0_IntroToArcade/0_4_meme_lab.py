
import arcade
import os

'''
Step 1: Download a blank meme image of your choice (keep it appropriate).  In pycharm create a directory, call it 'images',
in your project folder.  Copy and paste your meme image file into the images directory
'''

'''
Step 2: create a variable for each line of text of your meme,  assign text to the variables
'''
# put your code here

'''
Step 3: define a height and width variable and set them to the height and width of your meme image

'''
# put your code here

'''
Step 4: change the open_window command to use your height and width variables for the dimensions of the window
'''
arcade.open_window(600, 600, "Meme Generator")


arcade.start_render()

'''
Step 5:
Investigate the usage of the  arcade.load_texture command in the 0_2_drawing_primitives.py program.
Use the arcade.load_texture to set a texture variable to the image file of your meme.
'''
# put your code here

'''
Step 6: investigate and use the arcade.draw_texture_rectangle command to place your image in the center of the window
'''
# put your code here


'''
Step 7: Investigate the usage of the arcade.draw_text command and make the necessary calls to draw the lines of text
of your meme in the appropriate position 
'''
# put your code here


arcade.finish_render()

arcade.run()
