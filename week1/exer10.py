from ciscoconfparse import CiscoConfParse
import re
cfg = CiscoConfParse("cisco_ipsec.txt")

find_non_aes  = cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO',childspec=r'AES')

print "\n Crypto maps not using AES:"
for entry in find_non_aes:
    print entry.text
    for child in entry.children:
        if 'transform' in child.text:
            match = re.search('set transform-set (.*)$',child.text)
            trans_set = match.group(1)

    print "\nTransform set for this map is "+trans_set

