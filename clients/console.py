"""Airport List Query package.

Curses Console client module.
"""

import aplist
import urwid


class Query(object):
    """Package aplist and helpers in a single class."""

    def __init__(self):
        """Constructor."""
        apl = aplist.AirportList()
        self.retval = apl.query(query={})

    def get_list(self):
        """Return query result as a list of boxes."""
        list_ = list(map(
            urwid.Text, [self.get_result_str(ap) for ap in self.retval]))
        return list_

    def get_result_str(self, result):
        """Convert query result into a string."""
        str_ = ' '.join(map(str, result.values()))
        return str_

qy = Query()
al = urwid.ListBox(qy.get_list())

title = urwid.Text(u'Airport List Query - Console Application',
                   align='center')
status = urwid.Text(u'F1: Filter - F2: Sort')
text = (u'bla bla bla')

inner_frame = urwid.Frame(al, header=title, footer=status)

outer_frame = urwid.Frame(inner_frame, header=title, footer=status)

loop = urwid.MainLoop(outer_frame)
loop.run()


# if __name__ == '__main__':
#     main()
