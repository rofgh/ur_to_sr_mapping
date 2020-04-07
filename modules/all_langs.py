#language binary creator

with open("all_langs.txt", 'w') as f:
    for x in range(0, 8192):
        language = []
        for digit in format(x, '013b'):
            if digit == '0':
                language.append(0)
            if digit == '1':
                language.append(1)
        for x in language:
            f.write(str(x))
        f.write("\n")