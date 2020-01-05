import argparse
def get_params():
    parser = argparse.ArgumentParser(description='Simple version of the game "Life"', formatter_class=argparse.MetavarTypeHelpFormatter)
    parser.add_argument(
        '-ht',
        '--height',
        type=int,
        default=25,
        help='Height of game field (default: 25)'
    )
    parser.add_argument(
        '-wh',
        '--width',
        type=int,
        default=25,
        help='Width of game field (default: 25)'
    )
    
    parser.add_argument(
        '-i',
        '--iters',
        type=int,
        default=300,
        help='Max iterations (default: 300)'
    )

    def single_sym(string):
        if len(string) != 1:
            msg = "Length of symbol must be equal to 1"
            raise argparse.ArgumentTypeError(msg)
        return string

    parser.add_argument(
        '-f',
        '--fish',
        type=single_sym,
        default='!',
        help='Symbol of fish (default: "!")'
    )
    parser.add_argument(
        '-sh',
        '--shrimp',
        type=single_sym,
        default='@',
        help='Symbol of shrimp (default: "@")'
    )
    parser.add_argument(
        '-r',
        '--rock',
        type=single_sym,
        default='▲',
        help='Symbol of rock (default: "▲")'
    )
    parser.add_argument(
        '-e',
        '--empty',
        type=single_sym,
        default=' ',
        help='Symbol of empty cell (default: " ")'
    )
    return parser.parse_args()
