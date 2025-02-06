
coarses = ["MIT","Cybersecurity","Datascience"]
print(coarses)

# Accessing an element
print(coarses[2])

#Looping through an array
for a in coarses:
    print("Coarse is",a)
#Adding a new element into an array
coarses.append("Laravel")
print(coarses)


#Deleting an element from an array
coarses.remove("Cybersecurity")
print(coarses)