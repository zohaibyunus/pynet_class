from ciscoconfparse import CiscoConfParse

cfg = CiscoConfParse("cisco_ipsec.txt")

find_crypto = cfg.find_objects('^crypto map CRYPTO')

print "All crypto maps\n"
for i in find_crypto:
    print i.text

print "\nConfig for each map \n"

for i in find_crypto:
    print i.text
    for child in i.children:
        print child.text

