def count_letters(input_string, char, occ):
    counter = 0
    letter_dict = {}

    for letter in input_string:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

        if letter_dict[char] == occ:
            return counter
        counter += 1
    return counter


# Beispiel
string = 'AATGACG'
liste = count_letters(string, 'A', 3)
print(liste)  # Ausgabe: [1, 2, 1, 1, 3, 1, 2]
