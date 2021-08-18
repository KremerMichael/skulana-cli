import curses
import yaml

import skulana_serum


def run_command(command):

    if command == "SERUM":
        skulana_serum.serum(stdscr)
        return True
    return False

def skulana(stdscr):

    # setup colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    apps = ["SERUM", "RAYDIUM", "EXIT"]
    current_row = 0

    # Main loop
    running = True
    while running:

        # Print Apps display
        stdscr.clear()
        for index, app in enumerate(apps):

            # Determine placement offsets
            screen_height, screen_width = stdscr.getmaxyx()
            x = screen_width//2 - len(app)//2
            y = screen_height//2 + index

            # Check for active row
            pair = 1
            if index == current_row:
                pair = 2
            stdscr.attron(curses.color_pair(pair))
            stdscr.addstr(y, x, app)
            stdscr.attroff(curses.color_pair(pair))

        # Refresh new screen
        stdscr.refresh()

        # Grab character
        key = stdscr.getch()

        # Case: up arrow
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1

        # Case: down arrow
        elif key == curses.KEY_DOWN and current_row < (len(apps) - 1):
            current_row += 1

        # Case: enter key
        elif key == curses.KEY_ENTER or key in [10, 13]:

            # Temporarily shut down this curses setup
            stdscr.clear()

            # Run command
            command = apps[current_row]
            running = run_command(command)

    return


if __name__ == "__main__":
    curses.wrapper(skulana)
