def count_letters(input_string):
    result = []
    letter_dict = {}

    for letter in input_string:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

        result.append(letter_dict[letter])

    return result


# Beispiel
string = 'ABBAAAJKKJAKJKJ'
liste = count_letters(string)
print(liste)  # Ausgabe: [1, 2, 1, 1, 3, 1, 2]
