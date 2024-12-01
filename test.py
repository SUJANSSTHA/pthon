
shose1 = "nike"
shose2 = "addidas"
shose3 = "umbro"
shoes = ["nike","addidas","umbro"]
print(shoes[0])
print(shoes[-1])
print(shoes[0:2])
print(len(shoes))

shoes.append("infinity")
print(shoes)


shoes.insert(0,"hello") # !insert to first

# !dictonary
me = {
    "name": "Sujan",
    "age": 22
}
print(me["name"])
me["address"]=[ "Itahari"]
del me["address"]
print(me)
print(me.keys)
