"""Airport List Query package.

Command Line Interface client module.
"""


import aplist
import argparse


def parse():
    """Parse CLI arguments.

    Returns:
        (argparse.Namespace): Argument dict.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--search', nargs='+')
    parser.add_argument('-r', '--sort', nargs='+')
    parser.add_argument('-o', '--offset', type=int)
    parser.add_argument('-l', '--limit', type=int)
    return parser.parse_args()


def decode(contents):
    """Transform a list into a dict.

    Arguments:
        contents (list): list of pairs.

    Returns:
        (dict): pairs extracted from the contents list.
    """
    retval = {}
    for item in contents:
        k, v = item.split('=')
        if k in retval:
            raise ValueError('Key "{}" repeated'.format(k))
        retval[k] = v
    return retval


def main():
    """Script entry point."""
    query = {}
    args = parse()
    if args.search:
        query['search'] = decode(args.search)
    if args.sort:
        query['sort'] = decode(args.sort)
    if args.offset:
        query['page']['offset'] = decode(args.offset)
    if args.limit:
        query['page']['limit'] = decode(args.limit)

    apl = aplist.AirportList()
    retval = apl.query(query=query)
    print(retval)


if __name__ == '__main__':
    main()
