#!/usr/bin/env python3

import sys
import re
import ipaddress
import argparse



def main():
    """parse command line arguments, determine mode of operation"""

    parser = argparse.ArgumentParser(description='Collapse an arbitrary list of IP addresses into subnets of desired size.')

    # positional arguments
    #parser.add_argument('mode', action='store', choices=['init', 'action', 'show'], help='operating mode')
    parser.add_argument('-f', action='store', nargs='?', default='', help='input file name')
    parser.add_argument('-m', nargs='?', default='/24', help='smallest cidr subnet mask to apply (like /24)')
    parser.add_argument('-c', action='store_true', default=False, help='count IPs in each subnet')

    args = parser.parse_args()
    #print(type(args.profile))


    try:
        fh = open(args.f, 'r')
    except Exception as e:
        print("error opening input file: {}".format(e))
        sys.exit(1)

    mask = args.m

    iplist = []

    for line in fh.readlines():
        line = line.rstrip()
        iplist.append(line+mask)


    nets = [ipaddress.ip_network(_ip, strict=False) for _ip in iplist]
    cidrs = ipaddress.collapse_addresses(nets)

    counts = {}
    if args.c:
        print("counting per cidr")
        for cidr in cidrs:
            for ip in iplist:
                ip = re.sub("\/[0-9]*", "", ip)
                #print("is {} within {} ?".format(ip, cidr))
                if ipaddress.ip_address(ip) in cidr:
                    if cidr in counts:
                        counts[cidr] += 1
                    else:
                        counts[cidr] = 1

    for cidr in cidrs:
        if args.c:
            print("counting per cidr")
            try:
                print(cidr)
            except Exception as e:
                print(e)
            #print("{}: {}".format(cidr, counts[cidr]))
        else:
            print(cidr)



if __name__ == "__main__":
    main()