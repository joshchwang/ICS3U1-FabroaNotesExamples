import arcade

screen_width = 500
screen_height = 500
circle_lily_x = 0
circle_lily_y = 0
text_lily_x = 0
text_lily_y = 0

def draw_circle_lily(x, y):
    pass
    arcade.draw_circle_filled(200 + x,200+ y,50,arcade.color.AIR_FORCE_BLUE)
    arcade.draw_text("Lily",175 + x,200 + y,arcade.color.BLACK)


def on_draw(delta_time):

    arcade.start_render()
    global circle_lily_x, circle_lily_y,text_lily_x,text_lily_y
    draw_circle_lily(circle_lily_x,circle_lily_y)
    draw_circle_lily
    (text_lily_x,text_lily_y)
    circle_lily_x += 1
    circle_lily_y += 1
    text_lily_x += 1
    text_lily_y += 1


def main():
    arcade.open_window(screen_width, screen_height, "rada woo")
    arcade.set_background_color(arcade.color.WHITE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()