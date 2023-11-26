# Question 1 Write a Python program to read an entire text file.
file = open('President.csv', 'r') 
print(file.read())

# Question 2. Write a Python program to read the first n lines of a file.
with open('president.csv', 'r') as file:
    first_line = file.readline()
print("First line:", first_line)


 # Question 3. Write a Python program to read the last n lines of a file.
with open('president.csv', 'r') as file:
    for line in file.readlines()[-1:]:
        print(line)

# Question 4 Write a Python program that takes a text file as input and returns the number of words of a given text file.
file = open("president.csv", "rt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))

       








