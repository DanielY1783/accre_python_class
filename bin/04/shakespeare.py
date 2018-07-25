# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-25
#
# Description: My solution to the below exercise posed by Eric Appelt
#
# Exercise: Download the Complete Works of Shakespeare as a single text file.
# Open the file in python, read() the text, and use split() to split it into
# words. You can then use lower() and strip("'.,;:!?_-") to get rid of most
# punctuation and case. Use this list of words for the other exercises.
#
# Make a set of all words that start with z. Determine the length of the
# set. Make a set of all words that end in z. Make a union of the two sets,
# and determine its length.
#
# Make a dictionary where each word is a key and the value is the number of
# times that the given word appears in the text. How often do some common
# words like “and” and “the” appear?
#
# Using a dictionary comprehension, make a dictionary of only those words
# and their frequency where the frequency is over 1000. How many such words
# are there?
if __name__ == '__main__':
    with open("../../data/04/complete_shakespeare.txt", mode="r",
              encoding='utf-8') as input_file:
        # Get the list of words in lowercase
        words_list = input_file.read().split()

        # Format the words
        words_list = [word.strip("'.,;:!?_-").lower() for word in words_list]

        # Get set of words that start with "z"
        z_start_list = [word for word in words_list if word.startswith("z")]
        z_start_set = set(z_start_list)
        print("The length of the set of words from Shakespeare that start with "
              "'z' is {"
              "}".format(len(z_start_set)))

        # Make a set of words that end with "z"
        z_end_list = [word for word in words_list if word.endswith("z")]
        z_end_set = set(z_end_list)

        # Make union of set of words that start with "z" and set of words
        # that end with "z" and determine length
        z_start_end_set = z_start_set.union(z_end_set)
        print("The length of the set of words from Shakespeare that start "
              "or end with 'z' is {"
              "}".format(len(z_start_end_set)))

        # Create dictionary with words as keys and values as repetitions of
        # words
        word_count_dict = {}
        for word in words_list:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1

        # Print number of times that the words "the" and "and" appear
        print(
            """The word "the" appears {} times in Shakespeare's works""".format(
                word_count_dict["the"]))

        print(
            """The word "and" appears {} times in Shakespeare's works""".format(
                word_count_dict["and"]))

        # Make a dictionary with only words that appear over 1000 times and
        # print out the count of those words.
        frequent_words_dict = {word: count for word, count in
                               word_count_dict.items()
                               if count > 1000}

        print("The number of words that appear over 1000 times in "
              "Shakespeare's works is {}".format(len(frequent_words_dict)))