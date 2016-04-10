"""Airport List Query package.

Curses client module.
"""


import urwid


def test_exit_key(key):
    """Quit program if exit key was pressed.

    Arguments:
        key (input): Keyboard or mouse input.
    """
    if key in ['q', 'Q']:
        raise urwid.ExitMainLoop()


body = urwid.Filler(urwid.Divider(), 'top')
footer = urwid.Text(u'footer')
frame = urwid.Frame(urwid.AttrWrap(body, 'body'), footer=footer)

loop = urwid.MainLoop(frame)
loop.run()


# if __name__ == '__main__':
#     main()

"""

q: Quit
?: Help
F1: Open 'Search Dialog Box'
F2: Open 'Sort Dialog Box'
F3: Reverse Sort Order
F4: Change paginate options
F5: Clear search request


"""
