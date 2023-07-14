import os
from pathlib import Path

def model_new(name):
    path = Path(os.path.expanduser('~/.aurora/model/')) + name
    if os.path.exists(path):
        raise Exception('A model of the same name already exists.')
    os.mkdir(path)
    os.mkdir(path / 'departments')
