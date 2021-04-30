#!/usr/bin/env python3
import subprocess
import optparse
import re

#get_current_mac function returns the current MAC address
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    new_mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if (new_mac_search.group(0)):
        return(str(new_mac_search.group(0)))
    else:
        print("""Couldn't find the MAC of the interface.""")

#The get_arg() fuction is used to get arguments from user
def get_arg():
    parse=optparse.OptionParser()
    parse.add_option("-i","--interface", dest="interface", help="Takes interface to changes its MAC address")
    parse.add_option("-m","--mac", dest="mac", help="Takes desired MAC address")
    return parse.parse_args()

(options, values )= get_arg()
current_mac = str(get_current_mac(options.interface))
print('Current MAC of %s is %s'%(options.interface, current_mac))

#change_mac() function is used here to change the mac address of given interface to desired interface
def change_mac(interface, mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether",mac])
    subprocess.call(["ifconfig", interface, "up"])

change_mac(options.interface, options.mac)
current_mac = get_current_mac(options.interface)
print('New MAC is %s'%current_mac)