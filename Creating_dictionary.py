#dectionary
elemants = {"Ahmed": 1, "Mohamed" : 2, "farah": 3}
# using get function gives you none if the element is not in the dictionary 
# if the elemants in the dictionary gives you the value of the elemants 

print(elemants.get("Ahmed", "there is no qasim in the dictionary"))
print("bakar" in elemants)

print("////////////////////////////")

# using square brackets  gives you error if the element is not in the dictionary 
# if the elemants in the dictionary gives you the value of the elemants 
print(elemants["Ahmed"])
print(elemants["farah"])