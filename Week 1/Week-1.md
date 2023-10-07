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

## Problem 4

Your task is to count the number of different words in this text:

_ChatGPT has created this text to provide tips on creating interesting paragraphs. 
First, start with a clear topic sentence that introduces the main idea. 
Then, support the topic sentence with specific details, examples, and evidence.
Vary the sentence length and structure to keep the reader engaged.
Finally, end with a strong concluding sentence that summarizes the main points.
Remember, practice makes perfect!_

__Code:__

```
string = """
ChatGPT has created this text to provide tips on creating interesting paragraphs. 
First, start with a clear topic sentence that introduces the main idea. 
Then, support the topic sentence with specific details, examples, and evidence.
Vary the sentence length and structure to keep the reader engaged.
Finally, end with a strong concluding sentence that summarizes the main points.
Remember, practice makes perfect!
"""

# removing escape characters
string = string.replace('\n',' ')
string = string.replace('\t',' ')

# splitting words, and removing non-alphanumeric characters
word_list = string.split()
word_list = [word.strip(',.!') for word in word_list]

# getting the unique words
word_list = set(word_list)

word_dict = dict()

for word in word_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print("Count of words in the string: ")

for word in word_dict.keys():
    count = word_dict[word]
    print(word + " : " + str(count))
```

__Output:__

```
Count of words in the string: 
makes : 1
length : 1
structure : 1
end : 1
idea : 1
introduces : 1
specific : 1
examples : 1
a : 1
Finally : 1
the : 1
with : 1
perfect : 1
Vary : 1
that : 1
support : 1
has : 1
engaged : 1
on : 1
practice : 1
and : 1
ChatGPT : 1
Remember : 1
this : 1
provide : 1
sentence : 1
main : 1
details : 1
start : 1
First : 1
creating : 1
clear : 1
paragraphs : 1
concluding : 1
interesting : 1
created : 1
topic : 1
Then : 1
strong : 1
to : 1
text : 1
tips : 1
reader : 1
summarizes : 1
points : 1
keep : 1
evidence : 1
```

## Problem 5

Write a function that takes a word as an argument and returns the number of vowels in the word

__Code:__

```
def count_vowels(word):
    vowel_count = 0

    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in word:
        if letter in vowels:
            vowel_count += 1
    
    return vowel_count

input_word = "Alphabet"
print("Input Word: ", input_word)
print("Number of Vowels: " + str(count_vowels(input_word)))
```

__Output:__

```
Input Word:  Alphabet
Number of Vowels: 2
```
