def text():
    message = []
    with open("rulse.txt", "r", encoding = 'utf-8') as f_in:
        for line in f_in:
            message.append(line.rstrip())
    return message
