"""
    __Author__ : Sairaj Bhise
    Reference : None | Self made
    Difficulty : Medium

    Statement : Detective D hacked into terrorist's computer and had accessed his all mails. He founds a mail with
    encrypted message which has key with + or - operator assigned to it.
    write a program to decrypt the message using the key.

    Example:
        key = +1
        message = Anla gzr addm okzmsdc
        decrypted message = bomb has been planted

"""
from string import ascii_lowercase as alphabets


def decrypt(_key_, _message_, operator):
    decrypted_message = ""

    for letter in _message_:
        if letter == " ":
            decrypted_message = decrypted_message + letter
            continue

        index = list(alphabets).index(letter)
        if operator == "-":
            ans_key_index = index - _key_
        else:
            ans_key_index = index + _key_
        if ans_key_index > len(alphabets)-1:
            ans_key_index = ans_key_index - len(alphabets)
        decrypted_message = decrypted_message + alphabets[ans_key_index]

    return decrypted_message


if __name__ == "__main__":
    key = input()
    message = input().lower()
    _operator_ = key[0]
    print(decrypt(int(key[1:]), message, _operator_))
