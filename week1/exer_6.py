import yaml
import json

my_list = range(10)
my_list.append('Zohaib')
my_list.append({})
my_list[-1]['ipaddr']='10.1.1.1'
my_list[-1]['attr']=range(8)
#print "In list form: \n"+str(my_list)

#print "In YAML form: \n"+str(yaml.dump(my_list,default_flow_style=False))

with open("exer6_yaml.yml","w") as f:
    f.write(yaml.dump(my_list,default_flow_style=False))

##print "In JSON form: \n"+str(json.dumps(my_list)
with open("exer6_json.json","w") as f:
    json.dump(my_list,f)
