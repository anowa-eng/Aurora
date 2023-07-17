import os
import sys
from inspect import getmembers
from pathlib import Path

_PATH_TO_AURORA_MODEL_DIR = Path.home() / '.aurora' / 'model'

# Aurora private methods.

def _import_dept(path):
    sys.path.append(path)
    import main
    sys.path.remove(path)
    return main

_department_subdirectory_of_model = lambda model_name: _PATH_TO_AURORA_MODEL_DIR / model_name / 'dept'

def _get_all_department_names_under_model(model_name):
    department_directory = _department_subdirectory_of_model(model_name)
    paths = os.listdir(department_directory)
    return paths

class _Department:
    _NO_GENERATION_METHOD_FOUND_ERROR_MESSAGE = 'No `generate` method was provided. Please report this to the maintainer of the source code.'
    def __init__(self, model_name, department):
        self.name = department
        self.path = _department_subdirectory_of_model(model_name) / 'dept' / self.name
        self.path_as_string = str(self.path)
        self.module = _import_dept(self.path_as_string)
        self.can_generate = hasattr(self.module, 'generate')
        try:
            self.train = self.module.train
            self.can_train = True
        except NameError:
            self.can_Train = False
    def generate(self, **kwargs):
        try:
            self.module.generate(**kwargs)
        except NameError:
            raise NameError(_Department._NO_GENERATION_METHOD_FOUND_ERROR_MESSAGE)

class _Model:
    def __init__(self, name):
        self.name = name
        self.path = _PATH_TO_AURORA_MODEL_DIR / self.name
        self.departments = _get_all_department_names_under_model(self.name)
    @staticmethod
    def create_new(name):
        path = Path.home() / '.aurora' / 'model' / name
        if path.is_dir():
            raise Exception('A model of the same name already exists.')
        Path.mkdir(path)
        Path.mkdir(path / 'dept') # Departments folder
