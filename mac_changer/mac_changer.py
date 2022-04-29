import subprocess as sb
import optparse

#commands used to parse the user input when typing out the command from the command line
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac_address", help="New MAC address")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] You did not enter a usable interface")
    elif not options.new_mac_adress:
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
change_mac(options.interface, options.new_mac_address)
#add more code here
