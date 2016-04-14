"""Airport List Query package.

Curses Console client module.
"""

import aplist
import functools
import urwid


class Query(object):
    """Package aplist and helpers in a single class."""

    _fields = ['icao', 'iata', 'country', 'city']

    def __init__(self):
        """Constructor."""
        apl = aplist.AirportList()
        self.retval = apl.query(query={'page': {'offset': 0, 'limit': 10}})

    def get_list(self):
        """Return query result as a list of boxes."""
        clipped_text = functools.partial(urwid.Text, wrap='clip')
        list_ = list(map(
            clipped_text, [self.get_result_str(ap) for ap in self.retval]))
        return list_

    def get_result_str(self, result):
        """Convert query result into a string."""
        str_ = ' | '.join(map(str, [result.get(k) for k in self._fields]))
        return '| {} |'.format(str_)


def check_exit(key):
    """Check if the entered key matches the exit key."""
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


qy = Query()
al = urwid.ListBox(qy.get_list())

title = urwid.Text(u'Airport List Query - Console Application',
                   align='center')
status = urwid.Text(u'Q; Quit - F1: Filter - F2: Sort')
text = (u'bla bla bla')

inner_frame = urwid.Frame(al, header=title, footer=status)

outer_frame = urwid.Frame(inner_frame, header=title, footer=status)

loop = urwid.MainLoop(outer_frame, unhandled_input=check_exit)
loop.run()


# if __name__ == '__main__':
#     main()

"""

+----------
| Title Bar
+------+------+
| ICAO | IATA |
+------+------+
| LFPG | CDG  |

"""
