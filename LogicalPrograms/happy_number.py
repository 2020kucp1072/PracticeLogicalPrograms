'''
    @Author: VEMULA DILEEP
    @Date: 23-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 23-11-2024
    @Title : Happy number or not

'''

def is_happy(n):
    """
    Check if a number is a happy number.

    Parameters:
    n (int): Input number.

    Returns:
    bool: True if the number is happy, False otherwise.
    """
    seen =set()
    while n not in seen:
        seen.add(n)
        sum =0
        for i in str(n):
            sum +=int(i)**2
        if sum ==1:
            return "it is a happy number"
        n = sum
    return "it is not a happy number"
               

def main():
    print(is_happy(19))  # Output: True
    print(is_happy(2))  # Output: False

if __name__ == "__main__":
    main()
