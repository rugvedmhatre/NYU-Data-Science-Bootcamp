# Week 1 Practice

## Problem 1
Display Fibonacci Series upto 10 terms

__Code:__

```
fibonacci_numbers = []

# Adding the first two fibonacci numbers to the list
fibonacci_numbers.append(0)
fibonacci_numbers.append(1)

for i in range(2, 10):
    fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])

for number in fibonacci_numbers:
    print(number)
```

__Output:__

```
0
1
1
2
3
5
8
13
21
34
```

## Problem 2

Display numbers at the odd indices of a list

__Code:__

```
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("List: ", numbers_list)

print()
print("Numbers at Odd Indices of the list: ")

for i in range(len(numbers_list)):
    if i % 2 != 0:
        print(numbers_list[i])
```

__Output:__

```
List:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Numbers at Odd Indices of the list: 
2
4
6
8
10
12
14
```

## Problem 3

Print a list in reverse order

__Code:__

```
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print("List: ", days_of_the_week)

n = len(days_of_the_week)

print()
print("List in reverse order: ")
for i in range(n):
    print(days_of_the_week[(n - 1) - i])
```

__Output:__

```
List:  ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

List in reverse order: 
Sunday
Saturday
Friday
Thursday
Wednesday
Tuesday
Monday
```

