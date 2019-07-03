#!/usr/bin/env python3

import csv
from netaddr import IPNetwork

def exploder(subnet_list):
    ''' intakes a list of ip networks (in cidr notation)
    and exports a csv file of each ip address in that network '''

    hosts = []
    for subnet in subnet_list:
        expanded = [str(x) for x in IPNetwork(subnet)]
        hosts.extend(expanded)

    with open('exploded_subnets.txt', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for host in hosts:
            writer.writerow([host])

if __name__ == "__main__":
    with open('subnets.txt', 'r') as f:
        data = f.readlines()

    exploder([x.strip() for x in data])