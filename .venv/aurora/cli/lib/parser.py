import argparse

argparser = argparse.ArgumentParser()

argparser.add_argument('-n', '--api-logs-only', action='store_true')
subparsers = argparser.add_subparsers()

cmd_version_parser = argparser.add_argument('-v', '--version', action='store_true')

cmd_new_parser = subparsers.add_parser('new', help='Creates a new model.')
cmd_new_parser.add_argument('name_of_new_model')

cmd_train_parser = subparsers.add_parser('train')
cmd_train_parser.add_argument('model')