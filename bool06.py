def main(a):
    """
    Check the logic "The variable "a" is an even number"
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    if a%2==0:
        return True
    else:
        return False
    print(main(4)) # True
    print(main(7)) # False 