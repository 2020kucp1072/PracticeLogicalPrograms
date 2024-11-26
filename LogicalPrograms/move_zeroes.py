'''
    @Author: VEMULA DILEEP
    @Date: 23-11-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 23-11-2024
    @Title : move_zeroes

'''

def move_zeroes(nums):
    """
    Move all zeroes in the list to the end while maintaining order of non-zero elements.

    Parameters:
    nums (list): List of integers.

    Returns:
    list: List with zeroes moved to the end.
    """
    check =False
    index =0
    for i in range(len(nums)):
        if check!=True and nums[i]==0:
            check =True
            index =i
        elif nums[i]==0 or (check!=True and nums[i]!=0):
            continue
        else:
            temp =nums[i]
            nums[i]=nums[index]
            nums[index]=temp
            index = index +1
    return nums
            
            
        

def main():
    nums = [0, 1, 0, 3, 12, 0, 1, 0, 0]
    print(move_zeroes(nums))  
if __name__ == "__main__":
    main()