import os
import sys 

path = os.path.realpath(__file__)
DIR = path[:len(path) - len('/tests/test_config/__init__.py')]
sys.path.append(DIR)
DIR += '/app'
sys.path.append(DIR)
