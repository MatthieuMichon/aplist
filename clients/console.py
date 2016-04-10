"""Airport List Query package.

Curses client module.
"""


# import aplist
import urwid

status_footer = (u'Showing results 0 ~ 0 out of 0')
table_body = urwid.Filler(urwid.Divider(), 'top')
table_frame = urwid.Frame(urwid.AttrWrap(table_body, 'body'),
                          footer=status_footer)
table_filler = urwid.Filler(table_frame)

header_text = (u'Airport List Query - Console Application')
footer_text = (u' F1: Reset; F2: Filter; F3: Sort; F4: Export; '
               'Esc: Cancel; Q:quit')

header = urwid.Text(header_text, align='center')
body = urwid.Filler(urwid.Divider(), 'top')
footer = urwid.Text(footer_text)
# frame = urwid.Frame(urwid.AttrWrap(table_body, 'body'),
#                     header=header, footer=footer)
frame = urwid.Frame(table_filler,
                    header=header, footer=footer)

loop = urwid.MainLoop(frame)
loop.run()


# if __name__ == '__main__':
#     main()
