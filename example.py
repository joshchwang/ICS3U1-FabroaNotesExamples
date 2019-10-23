import arcade

screen_width = 400
screen_height = 400

box_x = 0
box_y = 0

def draw_box(x, y):
    arcade.draw_rectangle_filled(200 +x ,200+ y,75,75,arcade.color.UNIVERSITY_OF_TENNESSEE_ORANGE)



def on_draw(delta_time):

    arcade.start_render()

    global box_x, box_y
    draw_box(box_x,box_y)

    box_x += 1
    box_y += 1


def main():
    arcade.open_window(screen_width, screen_height, "box box")
    arcade.set_background_color(arcade.color.WHITE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()