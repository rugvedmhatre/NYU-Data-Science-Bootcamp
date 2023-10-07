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



