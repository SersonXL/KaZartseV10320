def caesar(text):
    a = input("Введите шифруемый текст: ")
    a = a.upper()
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    c = ''
    for i in a:
        place = alphabet.find(i)
        new_place = place + text
        if i in alphabet:
            c += alphabet[new_place]
        else:
            c += i
    print(c)


caesar(3)