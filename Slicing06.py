def main(s,n):
    """
    The s string variable is given. return all characters except n characters from the beginning.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    a = len(s)
    d = a - n
    q = s[-d:]
    return q 
print(main('jagcjg',2))