'''
    @Author: VEMULA DILEEP
    @Date: 25-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 25-11-2024
    @Title : kth smallest element

'''

def kth_smallest(nums, k):
    """
    Find the k'th smallest element in the array.

    Parameters:
    nums (list): List of integers.
    k (int): k'th position.

    Returns:
    int: k'th smallest element.
    """
    nums.sort()
    return nums[k - 1]

def main():
    nums = [7, 4, 6, 3, 9, 1]
    k = 3
    print(kth_smallest(nums, k))  # Output: 4

if __name__ == "__main__":
    main()
