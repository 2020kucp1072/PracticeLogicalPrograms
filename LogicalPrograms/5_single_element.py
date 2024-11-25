'''
    @Author: VEMULA DILEEP
    @Date: 23-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 23-11-2024
    @Title : finding the single element 

'''

def single_number(nums):
    """
    Find the number that appears only once in the list.

    Parameters:
    nums (list): List of integers.

    Returns:
    int: The single number.
    """
    result = 0
    for num in nums:
        result ^= num
    return result

def main():
    nums = [4, 1, 2, 1, 2]
    print(single_number(nums))  

if __name__ == "__main__":
    main()
