for x in range (1, 101):
    out = ''
    if x%2 == 0:
        out += "fizz"
    if x%3 == 0:
        out += "buzz"
    if out == '':
        out = x
    print(str(out))