import array as arr


def rev_integer(num):
    
    """
    Reverse an integer.

    Parameters:
    n (int): Input integer.

    Returns:
    int: Reversed integer.
    """
    rev =0
    while num>0:
        rem = num%10
        rev = rev*10 + rem
        num =num//10
    return rev
def main():
    
    num=int(input("enter the number to reverse: "))
    print(rev_integer(num))
    
    
if __name__=="__main__":
    main()
    