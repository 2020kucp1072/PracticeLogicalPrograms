import array as arr


def sum_two(arr,target):
    
    """
    Find indices of two numbers such that they add up to target.

    Parameters:
    nums (list): List of integers.
    target (int): Target sum.

    Returns:
    list: Indices of the two numbers.
    """
    res={}
    for i in range(len(arr)):
        diff = target -arr[i]
        if diff in res:
            return [res[diff],i]
        res[arr[i]]=i
        

def main():
    
    ar = arr.array('i',[2,12,34,11,10])
    target =int(input("enter the target: "))
    print(sum_two(ar,target))
    
    
if __name__=="__main__":
    main()
    