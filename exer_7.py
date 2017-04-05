import yaml
import json
from pprint import pprint as pp

with open("exer6_yaml.yml") as f:
    new_list = yaml.load(f)

pp(new_list)
