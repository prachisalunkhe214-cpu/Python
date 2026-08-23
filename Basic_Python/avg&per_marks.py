m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))


aggregate = m1 + m2 + m3 + m4 + m5


percentage = (aggregate / 500) * 100

# Display results
print("Aggregate Marks =", aggregate)
print("Percentage =", percentage, "%")
