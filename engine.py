import tdl

from input_handlers import handle_keys

# game engine
def main():
    #screeb size
    screen_width = 80
    screen_height = 50

    # player position
    player_x = int(screen_width/2)
    player_y = int(screen_height/2)

    # set the font
    tdl.set_font('arial10x10.png', greyscale=True, altLayout=True)

    # create the consoles
    root_console = tdl.init(screen_width, screen_height, title='Roguelike Tutorial Revised')
    con = tdl.Console(screen_width, screen_height)

    #game loop
    while not tdl.event.is_window_closed():

        # print @
        con.draw_char(player_x, player_y, '@', bg=None, fg=(255, 255, 255))
        root_console.blit(con, 0, 0, screen_width, screen_height, 0, 0)
        # show stuff on screen
        tdl.flush()
        # erase @ before drawing again
        con.draw_char(player_x, player_y, ' ', bg=None)

        # check if a key is pressed
        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                user_input = event
                break

        # no key pressed
        else:
            user_input = None

        if not user_input:
            continue
    
        action = handle_keys(user_input)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player_x += dx
            player_y += dy

        if not user_input:
            continue

        if exit:
            return True

        if fullscreen:
            tdl.set_fullscreen(not tdl.get_fullscreen())


if __name__ == '__main__':
    main()