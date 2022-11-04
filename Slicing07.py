def main(s,n):
    """
    The s string variable is given. return all characters except n characters at the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    return s[0:-n]
print(main('kmnkc',3))