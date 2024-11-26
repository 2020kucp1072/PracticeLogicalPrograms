'''
    @Author: VEMULA DILEEP
    @Date: 25-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 25-11-2024
    @Title : reverse vowles in a string

'''


def reverse_vowel_positions(string):
    """
    Reverse the positions of vowels in a given string.

    Parameters:
    string (str): Input string.

    Returns:
    str: String with vowels reversed in their positions.
    """
    index = []
    final = []
    check = {}
    vowels = "aeiouAEIOU"

    # Collect vowel indices and prepare the final list
    for i in range(len(string)):
        if string[i] in vowels:
            if string[i] in check:
                index.append(string.find(string[i], check[string[i]] + 1))
                check[string[i]] = string.find(string[i], check[string[i]] + 1)
            else:
                index.append(string.index(string[i]))
                check[string[i]] = string.index(string[i])
        final.append(string[i])

    # Sort the indices in reverse order
    sorted_list = sorted(index, reverse=True)

    # Replace vowels in the original string based on sorted order
    i = 0
    for j in sorted_list:
        final[index[i]] = string[j]
        i += 1

    # Convert the list back to a string
    return "".join(final)


# Example usage
def main():
    input_string = input("Enter a string: ")
    result = reverse_vowel_positions(input_string)
    print("String with reversed vowels:", result)


if __name__ == "__main__":
    main()
