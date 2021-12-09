"""
    __Author__ : Sairaj Bhise
    Reference : GeeksForGeeks | Self Modified
    Difficulty : Medium

    Statement : In a given array of size N find the continuous sub-array in which sum of all the elements of sub-array
    gives the value equal to S.
    Input : N and S , Array size of N
    Output : Sub-array

    Example
    S = 12
    Array = [1, 2, 3, 4, 5]

    Output = [3, 4, 5]
"""


def sub_array(s, arr):
    # Write your logic here


if __name__ == "__main__":
    S = int(input())
    _arr_ = list(map(int, input().split()))
    print(sub_array(S, _arr_))
