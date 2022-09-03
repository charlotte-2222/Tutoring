"""
Charlotte Childers
Built for Kate's Python Class
"""

import re

# regex to remove punctuation from words in text file
puncRegex = re.compile(r'[^a-zA-Z0-9\s]')


# error handle for no file
def noFile():
    print("No file found")


def wordCt():
    number_of_words = 0
    # Opening our text file in read only
    # mode using the open() function
    with open(r'sample_text.txt', 'r') as file:

        # reading content of the file and storing it in a variable
        data = file.read()

        # Splitting the data into separate lines
        lines = data.split()

        # Iterating over every word
        for word in lines:

            # checking if the word is numeric or not
            if not word.isnumeric():
                number_of_words += 1

    # Printing total number of words
    print(f"Word Count: ", number_of_words)


def avgLength():
    # reads average length of words in a text file
    with open(r'sample_text.txt', 'r') as file:
        data = file.read()
        lines = data.split()
        total = 0
        for word in lines:
            total += len(word)
        print("Average length: ", round(total / len(lines)))


def occurWord():
    # reads number of times a word appears in a text file
    # outputs to a text file
    print("Occurrence of words printed to a text file")
    with open(r'occurWord.txt', 'a') as f:
        f.write("Occurrence of words printed to a text file\n")
        f.write('{a:^8}{b:^2}{c:^8}'.format(a='Word', b="|", c='Occurrence'))
        f.write('\n-------------------\n')

    with open(r'sample_text.txt', 'r') as file:
        data = file.read()
        lines = data.split()
        occur = {}
        for word in lines:
            # removes punctuation from words
            word = puncRegex.sub('', word)
            occur[word] = occur.get(word, 0) + 1
        for word in occur:
            with open(r'occurWord.txt', 'a') as newfile:
                newfile.write("\t" + word + " -> " + str(occur[word]) + "\n")


def letterAlpha():
    # reads how many times words start with each letter of the alphabet
    # outputs to a text file
    print("Number of times a word starts with a letter printed to a text file")
    with open(r'letterAlpha.txt', 'a') as f:
        f.write("Number of times a word starts with a letter printed to a text file\n")
        f.write('{a:^8}{b:^2}{c:^8}'.format(a='Word', b="|", c='Occurrence'))
        f.write('\n-------------------\n')
    with open(r'sample_text.txt', 'r') as file:
        data = file.read()
        lines = data.split()
        for i in range(26):
            occur = 0
            for word in lines:
                if word[0] == chr(i + 97):
                    occur += 1
            with open(r'letterAlpha.txt', 'a') as newfile:
                newfile.write("\t" + chr(i + 97) + " -> " + str(occur) + "\n")


def main():
    wordCt()
    print("\n")
    avgLength()
    print("\n")
    occurWord()
    print("\n")
    letterAlpha()
    print("\n")


if __name__ == '__main__':
    try:
        main()
    except FileNotFoundError:
        noFile()
