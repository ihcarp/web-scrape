f1 = open("techs_website/tech_ggk.txt","r")
f2 = open("techs_website/tech_cognizant.txt","r")
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

print("Common technologies between ggk and cognizant:")
for tech in tech_list_1.intersection(tech_list_2):
    print(tech)

print("\n")
print("Technologies on cognizant but not ggk:")
for tech in tech_list_2.difference(tech_list_1):
    print(tech)

print("\n")
print("Technologies on ggk but not cognizant:")
for tech in tech_list_1.difference(tech_list_2):
    print(tech )



# print(tech_list_1.intersection(tech_list_2))
# print(tech_list_2.difference(tech_list_1))