import argparse

argparser = argparse.ArgumentParser()
subparsers = argparser.add_subparsers()

cmd_version_parser = argparser.add_argument('-v', '--version', action='store_true')

cmd_new_parser = subparsers.add_parser('new', help='Creates a new model.')
cmd_new_parser.add_argument('name')