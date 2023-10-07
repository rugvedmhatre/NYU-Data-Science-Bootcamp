# Your task is to count the number of different words in this text
# 	string = """
# 	ChatGPT has created this text to provide tips on creating interesting paragraphs. 
# 	First, start with a clear topic sentence that introduces the main idea. 
# 	Then, support the topic sentence with specific details, examples, and evidence.
# 	Vary the sentence length and structure to keep the reader engaged.
# 	Finally, end with a strong concluding sentence that summarizes the main points.
# 	Remember, practice makes perfect!
# 	"""

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