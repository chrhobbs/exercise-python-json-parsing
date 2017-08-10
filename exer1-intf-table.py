import json

with open('exer1-interface-data.json', 'r') as jsondata:
    interface_dict = json.load(jsondata)

imdata = interface_dict["imdata"]
phys, attr = "l1PhysIf", "attributes"

# List Comprehensions
intfs = [(i[phys][attr]["dn"], i[phys][attr]["descr"], i[phys][attr]["speed"], i[phys][attr]["mtu"]) for i in imdata]

print("=" * 90)
template = "{0:50} {1:20} {2:7} {3:6}"
print(template.format("DN", "Description", "Speed", "MTU"))
print(template.format("-" * 50, "-" * 20, "-" * 7, "-" * 6))

for i in intfs:
    print(template.format(*i))
