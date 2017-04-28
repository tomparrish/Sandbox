from urllib.request import urlopen
import xmltodict

with urlopen('https://download.microsoft.com/download/0/1/8/018E208D-54F8-44CD-AA26-CD7BC9524A8C/PublicIPs_20170417.xml') as fd:
    doc = xmltodict.parse(fd.read())
doc2 = doc.get('AzurePublicIpAddresses', {})
doc3 = doc2["Region"]
doc4 = doc3[3]
doc5 = list(doc4.values())[1]


tomth = ""
for item in doc5:
    for subnet in (item.values()):
        tomth = tomth + "\r\n" + subnet
print (tomth)
