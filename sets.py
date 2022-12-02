# set = a set is a collection which is unordered ,unindexed , no duplicate values

utensils = {"fork","spoon","cups","cups","cups"}# the set has no duplicate value which means even if i add multiple cups it will count as one cup
dishes = {"plates","teapot","saucer","cups"}

utensils.add("napkin")# adds stuff in set
utensils.remove("napkin")#removes stuff from a set
utensils.clear()# clears a set
utensils.update(dishes)#adds all the elements of a list(here dishes) to the specified list of utensils
dinner_table = dishes.union(utensils)#combines these sets into one
print(utensils.difference(dishes))# this will give what utensils has but dishes dont
print(utensils.intersection(dishes))# prints whats in common   

for x in utensils:
    print(x)

