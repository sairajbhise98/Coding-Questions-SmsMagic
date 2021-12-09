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
   # Write your logic here


if __name__ == "__main__":
    key = input()
    message = input().lower()
    _operator_ = key[0]
    print(decrypt(int(key[1:]), message, _operator_))
