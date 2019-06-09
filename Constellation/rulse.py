def text():
    with open("rulse.txt", "r", encoding = 'utf-8') as f_in:
        for line in f_in:
            print(line, end = "")
        print()
