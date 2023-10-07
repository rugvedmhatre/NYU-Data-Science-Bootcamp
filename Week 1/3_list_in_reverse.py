# Print a list in reverse order

days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print("List: ", days_of_the_week)

n = len(days_of_the_week)

print()
print("List in reverse order: ")
for i in range(n):
    print(days_of_the_week[(n - 1) - i])