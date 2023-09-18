#1108: Defanging an IP Address,Leetcode.com
def defanging_IPaddress(address):
    defanged_address = address.replace('.', '[.]')
    return defanged_address

ip_address = "127.0.0.1"
defanged_ip = defanging_IPaddress(ip_address)
print(defanged_ip)