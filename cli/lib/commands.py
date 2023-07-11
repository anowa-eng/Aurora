import os

def model_new(name):
    try:
        path = os.path.expanduser('~/.aurora/model/') + name
        os.mkdir(path)
        print(f'\n\u001b[0mAurora has created a model under the directory \n\u001b[0;32;1m{path}\n\u001b[0m.\nHave fun!\n')
    except Exception as e:
        print(e)
