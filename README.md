
# ipcollapse.py

Produce a list of consolidated CIDR-masked network ranges based on a arbitrary list of ip addresses.

## Example

```
$ python3 ipcollapse.py -f iplist -c /16
10.0.0.0/9
10.128.0.0/12
10.144.0.0/13
10.152.0.0/16
10.154.0.0/15
10.156.0.0/14
10.160.0.0/11
10.192.0.0/13
10.200.0.0/14
10.204.0.0/16
10.206.0.0/15
10.208.0.0/12
10.224.0.0/12
10.240.0.0/13
10.248.0.0/14
10.252.0.0/15
10.255.0.0/16
```

