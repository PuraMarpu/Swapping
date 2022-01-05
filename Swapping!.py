def swap():
    Usrinput1 = input()
    Usrinput2 = input()

    with open(Usrinput1, 'r') as f1:
        Read1 = f1.read()

    with open(Usrinput2, 'r') as f2:
        Read2 = f2.read()

    with open(Usrinput1, 'w') as f1:
        f1.write(Read2)

    with open(Usrinput2, 'w') as f2:
        f2.write(Read1)

    print(Read1)
    print(Read2)



swap()