import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

application = importlib.import_module('app').application
