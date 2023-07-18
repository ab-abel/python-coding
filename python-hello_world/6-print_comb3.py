# a 2 digit combinator programm

for i in range(0, 9):
    for n in range(i+1, 10):
        if(i<8):
            print("{}{}, ".format(i, n), end='')
        if(i>=8):
            print("{}{}".format(i, n), end='\n')
