import yaml
import json
from pprint import pprint as pp

with open("exer6_yaml.yml") as f:
    new_yaml_list = yaml.load(f)
with open("exer6_json.json") as f:
    new_json_list = json.load(f)

print "YAML list \n"
pp(new_yaml_list)
print "\n JSON list"
pp(new_json_list)
