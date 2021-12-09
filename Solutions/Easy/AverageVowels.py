"""
    __Author__ : Sairaj Bhise
    Reference : GeeksForGeeks | Self Made (Modified)
    Difficulty : Easy

    Statement : Find the percentage of vowels in a given string.
    Input : Wakanda Forever
    Output : 40.0

"""


def average(_string_):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    count = 0
    for letter in _string_:
        if letter in vowels:
            count = count + 1
    percentage = (count/len(_string_)) * 100
    return percentage


if __name__ == "__main__":
    S = input()
    print(average(S))
