import argparse
import sys
from lib import commands
from lib.parser import argparser
sys.path.append('./..')
from version.version import VERSION

args = argparser.parse_args(sys.argv[1:])
print(args)

if args.version:
    print(VERSION)
if args.name: commands.model_new(args.name)