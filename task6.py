def alphabet():
    Alphabet = 'abcdefghijklmnopqrstuvwxyz'
    a = 1
    b = {}
    for Alphabet in Alphabet:
        b[a] = Alphabet
        a += 1

    print(b)


alphabet()