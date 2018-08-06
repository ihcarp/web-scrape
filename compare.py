f1 = open("tech_industries_ggk.txt","r")
f2 = open("tech_industries_valuelabs.txt","r")
tech_list_1=set()
tech_list_2=set()
for line in f1:
    if not (line.__contains__(':')):
        tech_list_1.add(line.strip())
f1.close()

for line in f2:
    if not (line.__contains__(':')):
        tech_list_2.add(line.strip())
f2.close()

print("Common technologies between ggk and valuelabs:")
for tech in tech_list_1.intersection(tech_list_2):
    print(tech)

print("\n")
print("Technologies on valuelabs but not ggk:")
for tech in tech_list_2.difference(tech_list_1):
    print(tech)

print("\n")
print("Technologies on ggk but not valuelabs:")
for tech in tech_list_1.difference(tech_list_2):
    print(tech )



# print(tech_list_1.intersection(tech_list_2))
# print(tech_list_2.difference(tech_list_1))