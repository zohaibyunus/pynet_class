from ciscoconfparse import CiscoConfParse

cfg = CiscoConfParse("cisco_ipsec.txt")

pfs_2 = cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO',childspec=r'pfs group2')

print "\n Crypto maps using PFS group 2:"
for i in pfs_2:
    print i.text

