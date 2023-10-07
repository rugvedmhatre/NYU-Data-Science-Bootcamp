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

## Problem 6

Iterate through the following list of animals and print each one in all caps.
`animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']`

__Code:__

```
animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']

for animal in animals:
    print(animal.upper())
```

__Output:__

```
TIGER
ELEPHANT
MONKEY
ZEBRA
PANTHER
```

## Problem 7

Iterate from 1 to 15, printing whether the number is odd or even

__Code:__

```
for i in range(1, 16):
    if i % 2 == 0:
        print(str(i) + " : Even")
    else:
        print(str(i) + " : Odd")
```

__Output:__

```
1 : Odd
2 : Even
3 : Odd
4 : Even
5 : Odd
6 : Even
7 : Odd
8 : Even
9 : Odd
10 : Even
11 : Odd
12 : Even
13 : Odd
14 : Even
15 : Odd
```

## Problem 8

Take two integers as input from user and return the sum

__Code:__

```
number_1, number_2 = input("Input two numbers: ").split()

print("Sum of the two numbers: " + str(int(number_1) + int(number_2)))
```

__Output:__

```
Input two numbers: 3 8
Sum of the two numbers: 11
```

## Additional Challenge
1. Write a function that takes a movie dictionary from the above list and return true if imdb rating is greater than 5. Additionally, you can also alter the function to return whether the movie has low, medium or high rating

2. Write a function that accepts the entire list of movies and a category and returns the average score for that category.

3. Write a function that accepts the movie list and a category and returns all the movies belonging to that category. Your function should be able to throw an error if that category does not exist

```
# List of movies dictionaries:
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
```

__Code:__

```
def rating_more_than_5(movies, movie_name):
    for movie in movies:
        if movie['name'] == movie_name:
            return (movie['imdb'] > 5)

print("Movie Name: What is the name")
print("Rating above 5?", rating_more_than_5(movies, "What is the name"))
print()
print("Movie Name: Exam")
print("Rating above 5?", rating_more_than_5(movies, "Exam"))
print("---")
print()

def rating_category(movies, movie_name):
    for movie in movies:
        if movie['name'] == movie_name:
            if movie['imdb'] <= 10/3:
                return "Low"
            elif movie['imdb'] > 10/3 and movie['imdb'] <= 2 * 10/3:
                return "Medium"
            else:
                return "High"
            
print("Movie Name: What is the name")
print("Rating category : ", rating_category(movies, "What is the name"))
print()
print("Movie Name: Exam")
print("Rating category : ", rating_category(movies, "Exam"))
print()
print("Movie Name: AlphaJet")
print("Rating category : ", rating_category(movies, "AlphaJet"))
print("---")
print()

def average_of_category(movies, category):
    sum_of_ratings = 0
    number_of_movies = 0
    for movie in movies:
        if movie['category'] == category:
            sum_of_ratings += movie['imdb']
            number_of_movies += 1
    return sum_of_ratings/number_of_movies

print("Category: War")
print("Average Rating : ", average_of_category(movies, "War"))
print()
print("Category: Thriller")
print("Average Rating : ", average_of_category(movies, "Thriller"))
print("---")
print()

def get_movies_from_category(movies, category):
    movie_names = []
    for i in range(len(movies)):
        movie = movies[i]
        if movie['category'] == category:
            movie_names.append(movie['name'])
        if i == len(movies) - 1 and len(movie_names) == 0:
            raise Exception("Invalid Category!")
    return movie_names

print("Category: War")
print("Movies : ", get_movies_from_category(movies, "War"))
print()
print("Category: Romance")
print("Movies : ", get_movies_from_category(movies, "Romance"))
print()

try:
    print("Category: Mystery")
    print("Movies : ", get_movies_from_category(movies, "Mystery"))
    print()
except Exception as e:
    print(e)
```

__Output:__

```
Movie Name: What is the name
Rating above 5? True

Movie Name: Exam
Rating above 5? False
---

Movie Name: What is the name
Rating category :  High

Movie Name: Exam
Rating category :  Medium

Movie Name: AlphaJet
Rating category :  Low
---

Category: War
Average Rating :  3.2

Category: Thriller
Average Rating :  5.6
---

Category: War
Movies :  ['AlphaJet']

Category: Romance
Movies :  ['The Choice', 'Colonia', 'Love', 'Bride Wars', 'We Two']

Category: Mystery
Invalid Category!
```

