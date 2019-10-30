import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create a value that our snow_person1_x will start at.
snow_person1_x = 60
speed = 100


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)


def on_draw(delta_time):
<<<<<<< HEAD
    global snow_person1_x, snow_person1_y
=======
    global snow_person1_x
    global speed
>>>>>>> a5f2d146c8997911ebdbb01d886f70b756374750

    """ Draw everything """
    arcade.start_render()

    draw_grass()
    draw_snow_person(snow_person1_x, snow_person1_y)
    draw_snow_person(450, 180)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
<<<<<<< HEAD
    snow_person1_x += 1
    snow_person1_y += 1


# Create a value that our snow_person1_x will start at.
snow_person1_x = 150
snow_person1_y = 140
=======
    snow_person1_x += speed  

    #if snow_person1_x > 900:
    #    snow_person1_x = -100  
    if snow_person1_x > 740 or snow_person1_x < 60:
        speed = speed * -1
    
    #if snow_person1_x < 60:
    #    speed = speed * -1





>>>>>>> a5f2d146c8997911ebdbb01d886f70b756374750


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()