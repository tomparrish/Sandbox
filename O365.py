from urllib.request import urlopen
import xmltodict
import socket
import struct

def getnewaddresses(group):
    type = "IPv4"
    with urlopen('https://support.content.office.net/en-us/static/O365IPAddresses.xml') as o365:
        doc = xmltodict.parse(o365.read())
        doc2 = doc.get('products', {})
        doc3 = doc2.get('product', {})
        for i in range(len(doc3)):
            if group in doc3[i].values():
                doc4 = doc3[i]
        doc5 = list(doc4.values())[1]
        for i in range(len(doc5)):
            if type in doc5[i].values():
                doc6 = doc5[i]
        doc7 = list(doc6.values())[1]
    addresslist = ()
    for subnet in (doc7):
        subnet = cidr_to_netmask(subnet)
        tempaddresslist = "network-object " + subnet[0] + " " + subnet[1]
        tempaddresslist = tuple([tempaddresslist])
        addresslist = addresslist + tempaddresslist
    return addresslist
    
def getoldaddresses():
    addresslist = ( "network-object 157.56.53.128 255.255.255.128", "network-object 157.56.55.0 255.255.255.128", "network-object 157.56.58.0 255.255.255.128", "network-object 192.168.0.0 255.255.0.0" )
    return addresslist

def cidr_to_netmask(cidr):
# from http://stackoverflow.com/questions/33750233/convert-cidr-to-subnet-mask-in-python
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return network, netmask
    
def diff(list1, list2):
    new_list = []
    for element in list1:
        if element not in list2:
            new_list.append(element)
    return new_list
    
def presentdata(new_list, old_list):
    print ("These statements need to be added")
    for statement in new_list:
        print (statement)
    print ()
    print ()
    print ("These statements need to be removed")
    for statement in old_list:
        print (statement)

def main():
    newaddresslist = ()
    groups = ["o365", "Identity", "EOP"]
    for group in groups:
        newaddresslist = newaddresslist + getnewaddresses(group)
    oldaddresslist = getoldaddresses()
    new_list = diff(newaddresslist, oldaddresslist)
    old_list = diff(oldaddresslist, newaddresslist)
    presentdata(new_list, old_list)
 
main()
