"""
    __Author__ : Sairaj Bhise
    Reference : w3resource.com
    Difficulty : Hard

    Statement : Find the sum S of averages of next five and previous five palindrome of specified number N if and only
    if number N is palindrome itself else return False.
    Input :
        N : integer
    Output :
        S : integer

    Example :
       Input :  N = 99
       Output :  S = 187
"""


def sum_(n):
    previous_palindromes = []
    next_palindromes = []

    if str(n) == str(n)[::-1]:

        for x in range(n-1, 0, -1):
            if str(x) == str(x)[::-1]:
                previous_palindromes.append(x)
            if len(previous_palindromes) == 5:
                break

        y = n
        while True:
            y = y + 1
            if str(y) == str(y)[::-1]:
                next_palindromes.append(y)
            if len(next_palindromes) == 5:
                break

        answer = sum(previous_palindromes)//len(previous_palindromes) + sum(next_palindromes)//len(next_palindromes)
        return answer
    else :
        return False


if __name__ == "__main__":
    N = int(input())
    print(sum_(N))
