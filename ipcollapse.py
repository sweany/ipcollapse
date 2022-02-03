#!/usr/bin/env python3

import sys
import ipaddress
import argparse



def main():
    """parse command line arguments, determine mode of operation"""

    parser = argparse.ArgumentParser(description='Collapse an arbitrary list of IP addresses into subnets of desired size.')

    # positional arguments
    #parser.add_argument('mode', action='store', choices=['init', 'action', 'show'], help='operating mode')
    parser.add_argument('-f', action='store', nargs='?', default='', help='input file name')
    parser.add_argument('-c', nargs='?', default='/24', help='smallest cidr subnet mask to apply (like /24)')

    args = parser.parse_args()
    #print(type(args.profile))


    try:
        fh = open(args.f, 'r')
    except Exception as e:
        print("error opening input file: {}".format(e))
        sys.exit(1)

    mask = args.c

    iplist = []

    for line in fh.readlines():
        line = line.rstrip()
        iplist.append(line+mask)


    nets = [ipaddress.ip_network(_ip, strict=False) for _ip in iplist]
    cidrs = ipaddress.collapse_addresses(nets)

    for cidr in cidrs:
        print(cidr)



if __name__ == "__main__":
    main()