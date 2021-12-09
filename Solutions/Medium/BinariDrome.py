"""
    __Author__ : Sairaj Bhise
    Reference : IncludeHelp.com
    Difficulty : Medium

    Statement : For a given integer check if the binary form of that number is palindrome or not.
    Input : N
    Output : Boolean

    Example :
    N = 27
    Output : True
"""


def check(n):
    binary_form = int(bin(n)[2:])
    reversed_binary_form = str(binary_form)[::-1]

    if int(reversed_binary_form) == binary_form:
        return True
    else:
        return False


if __name__ == "__main__":
    N = int(input())
    print(check(N))
