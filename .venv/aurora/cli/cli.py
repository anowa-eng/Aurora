import sys
import opencc
import json
from lib.parser import argparser
from lib.shell.shell import shell
sys.path.append('./..')
from version.version import VERSION
from sdk.main import _Model

cmd = sys.argv[1]
args = argparser.parse_args(sys.argv[1:])

if hasattr(args, 'version'):
    if args.version:
        print(VERSION)

if cmd == 'new':
    try:
        _Model.create_new(args.name)
        api_log = json.dumps({ 'ok': True })
        print(f'Created a new model under \u001b[1m{args.name}')
    except Exception as e:
       print(e)

if cmd == 'shell':
    shell()
