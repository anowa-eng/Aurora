def _read_input(cmd, model):
    print(cmd)

def shell(model):
    terminal_header = f'[{model}@aurora]$ '
    user_has_quit = False
    while not user_has_quit:
        cmd = input(terminal_header)
