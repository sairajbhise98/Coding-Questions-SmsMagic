"""
    __Author__ : Sairaj Bhise
    Reference : Tcs Ninja Questions
    Difficulty : Easy

    Statement : For a give list of numbers, find the lowest possible number which cannot be achieved even if all the
    numbers from list are added together.

    Input format :
        N = int
        Array = Array of Size N

    Output :
        Answer = int

    Example :
        N = 5
        Array = [1, 2, 3, 4, 5]
        Answer = 16

"""


def solve(array):
    # Write your logic here


N = int(input())
A = [int(input()) for i in range(0, N)]
print(solve(A))
