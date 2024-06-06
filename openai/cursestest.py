import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Display text with different attributes
    stdscr.addstr("Normal text\n", curses.A_NORMAL)
    stdscr.addstr("Bold text\n", curses.A_BOLD)
    stdscr.addstr("Underlined text\n", curses.A_UNDERLINE)
    stdscr.addstr("Reverse video text\n", curses.A_REVERSE)
    stdscr.addstr("Standout text\n", curses.A_STANDOUT)
    stdscr.addstr("Blinking text\n", curses.A_BLINK)
    stdscr.addstr("Dim text\n", curses.A_DIM)
    stdscr.addstr("Italic text\n", curses.A_ITALIC)

    # Refresh the screen
    stdscr.refresh()

    # Wait for user input
    stdscr.getkey()

# Initialize curses
curses.wrapper(main)
