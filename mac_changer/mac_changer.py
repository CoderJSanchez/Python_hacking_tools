import subprocess as sb
import optparse
import re

#commands used to parse the user input when typing out the command from the command line
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac_address", help="New MAC address")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] You did not enter a usable interface")
    elif not options.new_mac_address:
        parser.error("[-] You did not enter a usable MAC address")
    return options


#function that runs the commands to change the MAC address
def change_mac(interface, new_mac_address):
    print(f'[+] Changing MAC address for {interface}')

    sb.call(["ifconfig", interface, "down"])
    sb.call(["ifconfig", interface, "hw", "ether", new_mac_address])
    sb.call(["ifconfig", interface, "up"])

    print(f"[+] MAC address change to {new_mac_address} is complete")



#calling the function change_mac() that was created at the top
options = get_arguments()
#change_mac(options.interface, options.new_mac_address)

ifconfig_result = str(sb.check_output(["ifconfig", options.interface]))


mac_address_search_result  = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
if mac_address_search_result:
    print(f'Your MAC address of {mac_address_search_result} is being changed to something else.')
else:
    print("[-] Could not read MAC address")