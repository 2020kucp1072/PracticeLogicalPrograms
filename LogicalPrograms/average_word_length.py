'''
    @Author: VEMULA DILEEP
    @Date: 23-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 23-11-2024
    @Title : average word length

'''

import re

def average_word_length(sentence):
    """
    Calculate the average word length of a sentence.

    Parameters:
    sentence (str): Input sentence.

    Returns:
    float: Average word length.
    """
    words = re.findall(r'\b\w+\b', sentence)
    return sum(len(word) for word in words) / len(words)

def main():
    sentence = "Hi all, my name is Tom...I am originally from Australia."
    print(average_word_length(sentence)) 

if __name__ == "__main__":
    main()
