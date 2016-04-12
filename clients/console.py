"""Airport List Query package.

Curses Console client module.
"""

import aplist
import urwid


class Query(object):

    def __init__(self):
        apl = aplist.AirportList()
        self.retval = apl.query(query={})


qy = Query()
al = urwid.ListBox([qy.retval])

title = urwid.Text(u'Airport List Query - Console Application',
                   align='center')
status = urwid.Text(u'F1: Filter - F2: Sort')
text = (u'bla bla bla')

inner_frame = urwid.Frame(
    urwid.Filler(al), header=title, footer=status)

outer_frame = urwid.Frame(inner_frame, header=title, footer=status)

loop = urwid.MainLoop(outer_frame)
loop.run()


# if __name__ == '__main__':
#     main()
