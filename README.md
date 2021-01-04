# cidr-exclude.py
This script is used for excluding Network 2 from Network 1 in large quantities, suited to all following scenarios:

1. Network 1 and 2 has no overlap;
2. Network 1 and 2 has overlap, but not entirely subnetted to each other;
3. Network 1 is Network 2's subnet.
4. Network 1 is Network 2's supernet.

Either Networks can be a list of IP/CIDR. Due my test it can still work when netmask reaches /8. Output will be in the format of CIDR as well.


