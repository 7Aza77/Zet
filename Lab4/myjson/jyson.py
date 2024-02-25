import json

with open("sample_data.json", "r") as my_file:
    json_string = my_file.read()

data = json.loads(json_string)

interfaces = data.get('imdata', [])


print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50, "-" * 20, "-" * 8, "-" * 6)

for interface in interfaces[1:]:
    l1_phys_if = interface.get('l1PhysIf', {})
    attributes = l1_phys_if.get('attributes', {})
    
    dn = attributes.get('dn', '')
    description = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')
    
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))