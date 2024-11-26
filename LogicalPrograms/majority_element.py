'''
    @Author: VEMULA DILEEP
    @Date: 23-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 23-11-2024
    @Title : Majority element

'''

def find_majority_element(nums):
    """
    Find the majority element in the list.

    Parameters:
    nums (list): List of integers.

    Returns:
    int: The majority element.
    """
    candidate, count = None, 0

    #Find a candidate
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    #Verify the candidate
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None


def main():
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(find_majority_element(nums))  # Output: 2

if __name__ == "__main__":
    main()
