import sys
import opencc
import json
from lib import commands
from lib.parser import argparser
sys.path.append('./..')
from version.version import VERSION

args = argparser.parse_args(sys.argv[1:])

if hasattr(args, 'version'):
    if args.version:
        print(VERSION)
if hasattr(args, 'name_of_new_model'):
    try:
        commands.model_new(args.name_of_new_model)
        api_log = json.dumps({ 'ok': True })
        print(api_log if args.api_logs_only else f'Created a new model under \u001b[1m{arg}')
    except Exception as e:
        if args.api_logs_only:
            msg = json.dumps({
                'ok': False,
                'error': str(e)
            })
            print(msg)
        else:
            print('Created a ')
    