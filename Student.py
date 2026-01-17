# Input marks
m1, m2, m3, m4, m5 = map(int, input("Enter marks of 5 subjects: ").split())

# Calculate total
total = m1 + m2 + m3 + m4 + m5

# Calculate percentage
percentage = (total / 500) * 100

# Output results
print("Total Marks =", total)
print("Percentage =", percentage, "%")
