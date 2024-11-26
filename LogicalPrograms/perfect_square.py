'''
    @Author: VEMULA DILEEP
    @Date: 23-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 23-11-2024
    @Title : perfect sqaure

'''

def is_perfect_square(n):
    """
    Check if a number is a perfect square.

    Parameters:
    n (int): Input number.

    Returns:
    bool: True if perfect square, False otherwise.
    """
    check = n**(1/2)
    
    if check ==int(check):
      return "it is a perfect square"
    return "it is not a perfect square"
    
def main():
    print(is_perfect_square(25))  # Output: True
    print(is_perfect_square(20))  # Output: False

if __name__ == "__main__":
    main()